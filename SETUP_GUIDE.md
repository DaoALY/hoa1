# 🚀 HOA Stories Generator - Setup Guide

## Tóm tắt hệ thống

```
┌─────────────────────────────────────┐
│ Frontend (Claude Artifact)          │
│ - UI để nhập keyword                │
│ - Hiển thị videos trending          │
│ - Copy kịch bản                     │
└──────────────┬──────────────────────┘
               │
               │ Call /api/analyze
               ▼
┌─────────────────────────────────────┐
│ Backend (Vercel)                    │
│ - YouTube API → Fetch trending      │
│ - Extract subtitles từ videos       │
│ - Return data cho frontend          │
└──────────────┬──────────────────────┘
               │
               │ Return context
               ▼
┌─────────────────────────────────────┐
│ Claude API (từ nick khác)           │
│ - Nhận context từ backend           │
│ - Generate kịch bản mới             │
│ - Hiển thị kết quả                  │
└─────────────────────────────────────┘
```

---

## ✅ Bước 1: Chuẩn bị

### 1.1 YouTube API Key
1. Vào https://console.cloud.google.com
2. Create new project
3. Enable "YouTube Data API v3"
4. Create API Key (Credentials)
5. Copy key

### 1.2 Claude API Key
- Vào https://console.anthropic.com
- Get API Key (dùng cho artifact sau)

---

## 📦 Bước 2: Deploy Backend lên Vercel

### 2.1 Setup Files
Bạn đã có:
- `backend.py` ✅
- `requirements.txt` ✅
- `vercel.json` ✅

### 2.2 Upload lên GitHub
```bash
# Tạo folder project
mkdir hoa-script-generator
cd hoa-script-generator

# Copy files
cp backend.py .
cp requirements.txt .
cp vercel.json .
cp README.md .

# Git init
git init
git add .
git commit -m "Initial commit"
```

### 2.3 Push lên GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/hoa-script-generator.git
git branch -M main
git push -u origin main
```

### 2.4 Deploy Vercel
1. Vào https://vercel.com
2. Import GitHub project
3. Select repository
4. Add Environment Variable:
   - Name: `YOUTUBE_API_KEY`
   - Value: **(Paste YouTube API Key của bạn)**
5. Click Deploy

**Bạn sẽ nhận được:** `https://your-app-name.vercel.app`

---

## 🎨 Bước 3: Tạo Frontend Artifact

### 3.1 Copy frontend.jsx
Tôi sẽ tạo 1 **Artifact** với code từ `frontend.jsx`

### 3.2 Cấu hình Artifact
Trong artifact, bạn sẽ:
1. **Điền Backend URL**: `https://your-app-name.vercel.app` (từ Vercel)
2. **Nhập Claude API Key** khi click Generate
3. Bấm **Generate** → code sẽ:
   - Call backend → lấy trending videos
   - Call Claude API → generate kịch bản

---

## 🧪 Bước 4: Test

### Test 1: Backend
```bash
curl -X POST https://your-app.vercel.app/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"keyword":"HOA stories"}'
```

Kết quả: Sẽ trả về videos + subtitles context

### Test 2: Artifact
1. Vào artifact
2. Điền: `https://your-app-name.vercel.app`
3. Click Generate
4. Nhập Claude API Key khi được hỏi
5. Chờ kịch bản xuất hiện ✨

---

## 📊 Lưu ý

### Backend (Vercel)
- ✅ Miễn phí
- ✅ Tự động scale
- ⚠️ Cold start ~5 giây (lần đầu)
- ⚠️ Giới hạn 100GB/tháng bandwidth (enough)

### Frontend (Artifact)
- ✅ Chạy trên Claude website
- ✅ Ai cũng dùng được
- ⚠️ Cần Claude API Key (người dùng nhập)
- ⚠️ Không phải Public Link, chỉ dùng trong Claude

---

## 🔄 Quy trình hàng ngày

**Người dùng (bất kỳ nick Claude nào):**

1. Vào artifact (bạn share)
2. Nhập keyword: "hoa stories"
3. Click Generate
4. Nhập Claude API Key (của họ)
5. Chờ ~10 giây
6. → Kịch bản mới xuất hiện
7. Copy paste vào project rendering của bạn

---

## 🆘 Troubleshooting

### "Backend not found"
- ✅ Check URL Vercel có đúng không
- ✅ Vercel deploy thành công chưa?

### "Claude API error"
- ✅ Check API Key đúng chưa
- ✅ API Key có đủ quota không?

### "No videos found"
- ✅ YouTube API Key setup chưa?
- ✅ Keyword hợp lệ chưa?

---

## 📝 Tóm tắt chi phí

| Service | Cost | Note |
|---------|------|------|
| Vercel | FREE | 100GB/month |
| YouTube API | FREE | 10k units/day |
| Claude API | PAY | User dùng key của họ |

**Total cost for you: FREE** (trừ Claude API là user trả)

---

## ❓ Câu hỏi?

Cần help? Hãy nhắn tôi link artifact + error message.
