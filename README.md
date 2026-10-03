# HOA Stories Script Generator

Backend để fetch trending HOA videos + extract subtitles từ YouTube.
Frontend (Artifact) sẽ call backend này + Claude API để generate kịch bản mới.

## 🏗️ Architecture

```
Frontend (Claude Artifact)
    ↓
Backend (Vercel) - YouTube API → Get videos + subtitles
    ↓
Claude API (từ nick khác) → Generate screenplay
```

## 🚀 Setup Vercel

### 1. Chuẩn bị
- Đăng ký Vercel (miễn phí): https://vercel.com
- YouTube API Key (từ Google Cloud Console)

### 2. Deploy
```bash
git clone <repo>
cd <folder>
vercel
```

### 3. Set Environment Variables
Trong Vercel Dashboard:
- `YOUTUBE_API_KEY` = API key của YouTube

### 4. Test
```
POST https://your-app.vercel.app/api/analyze
{
  "keyword": "HOA stories"
}
```

## 📝 API Endpoint

**POST** `/api/analyze`

Body:
```json
{
  "keyword": "HOA stories"
}
```

Response:
```json
{
  "success": true,
  "videos": [
    {
      "title": "...",
      "videoId": "...",
      "thumbnail": "...",
      "subtitles": "..."
    }
  ],
  "context": "Combined subtitle context for Claude",
  "timestamp": "2026-10-03T..."
}
```

## 🏃 Chạy Local
```bash
pip install -r requirements.txt
export YOUTUBE_API_KEY=your_youtube_api_key
python backend.py
```

Sau đó test endpoint `/api/analyze`
