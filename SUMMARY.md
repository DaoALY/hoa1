# 📋 HOA Stories Generator - Summary

## ✅ Files đã tạo cho bạn

### Backend (Vercel)
- **backend.py** - Flask API server
  - `POST /api/analyze` - Fetch YouTube videos + extract subtitles
  - `GET /api/health` - Health check
  
- **requirements.txt** - Python dependencies
  - flask, flask-cors, google-api-python-client, yt-dlp, pysrt, gunicorn
  
- **vercel.json** - Vercel config
  - Environment: YOUTUBE_API_KEY only
  - Max duration: 300s

### Frontend (Artifact - React)
- **frontend.jsx** - React interactive app
  - Input keyword
  - Config backend URL
  - Call backend `/api/analyze`
  - Display trending videos
  - Call Claude API for screenplay generation
  - Copy to clipboard

### Documentation
- **README.md** - API documentation
- **SETUP_GUIDE.md** - Hướng dẫn chi tiết từ A-Z
- **SUMMARY.md** - File này

---

## 🎯 Cách hoạt động

```
1. User vào Artifact (bạn share)
   ↓
2. Nhập keyword: "hoa stories"
   ↓
3. Click Generate
   ↓
4. Frontend gọi backend /api/analyze
   ↓
5. Backend:
   - YouTube API → Tìm trending videos
   - yt-dlp → Tải subtitles
   - Return videos + subtitle context
   ↓
6. Frontend nhận data + gọi Claude API
   ↓
7. Claude sinh kịch bản mới dựa trên context
   ↓
8. Kịch bản hiển thị + copy được
```

---

## 🚀 Các bước tiếp theo

### Phase 1: Deploy Backend (1-2 giờ)
1. [ ] Copy files vào folder
2. [ ] Push lên GitHub
3. [ ] Deploy Vercel + set YouTube API Key
4. [ ] Test `/api/analyze` endpoint
5. [ ] Lấy Vercel URL

### Phase 2: Tạo Artifact (30 phút)
1. [ ] Tôi tạo React artifact từ `frontend.jsx`
2. [ ] Bạn điền Vercel URL vào artifact
3. [ ] Test: Generate kịch bản

### Phase 3: Chia sẻ (ngay)
1. [ ] Share artifact link
2. [ ] Ai cũng dùng được
3. [ ] Mỗi ngày → 1 kịch bản mới

---

## 🔑 API Keys cần

| Key | Dùng ở đâu | Ai cần |
|-----|-----------|-------|
| YouTube API | Backend (Vercel) | BẠN - set environment var |
| Claude API | Frontend (Artifact) | NGƯỜI DÙNG - nhập khi generate |

---

## 💰 Chi phí

- **Vercel**: FREE (100GB/month)
- **YouTube API**: FREE (10k units/day)
- **Claude API**: Pay-as-you-go (người dùng trả)
  - ~$0.003 per screenplay

---

## 📱 Features

✅ Auto fetch trending HOA videos  
✅ Extract + process subtitles  
✅ Generate original Vietnamese screenplay  
✅ Display video thumbnails  
✅ Copy kịch bản to clipboard  
✅ No setup needed for users (chỉ paste link)  
✅ 24/7 online (Vercel)  

---

## 🎬 Ví dụ workflow

**Sáng hôm nay:**
1. Bạn muốn 1 kịch bản HOA mới
2. Vào artifact → nhập "hoa stories"
3. Bấm Generate → 30 giây
4. Copy kịch bản → paste vào project rendering
5. Render video như bình thường

**Ngày mai:**
- Lặp lại quy trình

---

## ⚙️ Customization (sau này)

Bạn có thể:
- Đổi `MAX_VIDEOS` (lấy bao nhiêu video)
- Đổi `SPLIT_COUNT` (ghép bao nhiêu subtitle)
- Thêm prompt guidelines cho Claude
- Đổi keyword mặc định
- Thêm prompt context rules

---

## 📞 Support

Nếu có vấn đề:
1. Check SETUP_GUIDE.md troubleshooting section
2. Test backend: `curl https://your-app.vercel.app/api/analyze`
3. Check error logs ở Vercel Dashboard
4. Nhắn tôi error message + link artifact

---

**Status: Ready to deploy! ✨**

Bạn muốn tôi tạo artifact ngay, hay bạn muốn tự setup backend trước?
