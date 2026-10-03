import os
import re
import json
from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify, request
from flask_cors import CORS
from googleapiclient.discovery import build
import yt_dlp
import pysrt

app = Flask(__name__)
CORS(app)

# ============ CONFIG ============
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "YOUR_YOUTUBE_API_KEY_HERE")
KEYWORD = "HOA stories"
LANG_CODE = "en"
MAX_VIDEOS = 4
SPLIT_COUNT = 4
# ================================

def fetch_subtitles(video_id):
    """Tải subtitle từ YouTube"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': [LANG_CODE],
        'subtitlesformat': 'srt',
        'skip_download': True,
        'outtmpl': '/tmp/%(id)s'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
        
        # Tìm file srt
        for f in os.listdir('/tmp'):
            if video_id in f and (f.endswith(f'.{LANG_CODE}.srt') or f.endswith('.srt')):
                return os.path.join('/tmp', f)
        return None
    except Exception as e:
        print(f"Error fetching subtitles: {e}")
        return None

def process_subtitles(srt_file):
    """Xử lý subtitle thành kịch bản"""
    try:
        subs = pysrt.open(srt_file, encoding='utf-8')
    except:
        subs = pysrt.open(srt_file, encoding='latin-1')
    
    def clean_text(text):
        text = re.sub(r'\[[^\]]*\]', ' ', text, flags=re.IGNORECASE)
        text = re.sub(r'>+', ' ', text)
        text = re.sub(r'[^\w\s.?!,\'"-]', ' ', text, flags=re.UNICODE)
        return re.sub(r'\s+', ' ', text).strip()
    
    all_text = [clean_text(sub.text.replace('\n', ' ')) for sub in subs if sub.text.strip()]
    full_text = " ".join(all_text)
    full_text = re.sub(r'\s+([.?!])', r'\1', full_text)
    full_text = re.sub(r'([.?!])', r'\1 ', full_text)
    full_text = re.sub(r'\s+', ' ', full_text).strip()
    
    # Split sentences
    sentences = re.split(r'(?<=[.?!])\s+', full_text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Group sentences
    grouped = [" ".join(sentences[i:i+SPLIT_COUNT]) for i in range(0, len(sentences), SPLIT_COUNT)]
    
    return "\n\n".join(grouped)

def get_trending_videos(keyword):
    """Lấy trending videos từ YouTube API"""
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    now = datetime.now(timezone.utc)
    published_after = (now - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    try:
        search_req = youtube.search().list(
            q=keyword,
            part="snippet",
            type="video",
            maxResults=MAX_VIDEOS,
            order="viewCount",
            videoDuration="long",
            publishedAfter=published_after
        )
        response = search_req.execute()
        videos = []
        for item in response.get('items', []):
            videos.append({
                'videoId': item['id']['videoId'],
                'title': item['snippet']['title'],
                'thumbnail': item['snippet']['thumbnails']['default']['url']
            })
        return videos
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """API endpoint to analyze trending HOA videos and extract subtitles"""
    data = request.json
    keyword = data.get('keyword', KEYWORD)
    
    try:
        # 1. Get trending videos
        videos = get_trending_videos(keyword)
        if not videos:
            return jsonify({'error': 'No videos found'}), 404
        
        # 2. Extract subtitles from top videos
        videos_data = []
        for i, video in enumerate(videos[:3], 1):
            print(f"Processing video {i}: {video['title']}")
            srt_file = fetch_subtitles(video['videoId'])
            if srt_file:
                script_text = process_subtitles(srt_file)
                videos_data.append({
                    'title': video['title'],
                    'videoId': video['videoId'],
                    'thumbnail': video['thumbnail'],
                    'subtitles': script_text[:800]  # First 800 chars
                })
                try:
                    os.remove(srt_file)
                except:
                    pass
        
        if not videos_data:
            return jsonify({'error': 'Failed to process videos'}), 500
        
        # 3. Combine context for Claude
        combined_context = "\n\n".join([
            f"=== {v['title']} ===\n{v['subtitles']}" 
            for v in videos_data
        ])
        
        return jsonify({
            'success': True,
            'videos': videos_data,
            'context': combined_context,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=False, port=int(os.getenv('PORT', 3000)))
