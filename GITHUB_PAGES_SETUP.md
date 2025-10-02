# 🌐 GitHub Pages Setup Guide

Deploy your chatbot to GitHub Pages for **100% FREE** hosting!

---

## 🎯 **Two Deployment Options**

### **Option A: Serverless (Easiest - Recommended)**
- ✅ Everything on GitHub Pages
- ✅ No backend needed
- ✅ 100% free
- ⚠️ API key visible in browser code

### **Option B: Backend + Frontend**
- ✅ More secure (API key hidden)
- ✅ Frontend on GitHub Pages
- ⏳ Backend needs Railway/Render

---

## 🚀 **Option A: Serverless Deployment (5 minutes)**

I've created a serverless version in the `docs/` folder that works entirely on GitHub Pages!

### **Step 1: Enable GitHub Pages**

1. Go to your repository: https://github.com/jai-nayani/jai-llm-chatbot

2. Click **Settings** (top right)

3. Scroll down to **Pages** section (left sidebar)

4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/docs`

5. Click **Save**

6. Wait 1-2 minutes for deployment

7. **Your site will be live at:**
   ```
   https://jai-nayani.github.io/jai-llm-chatbot/
   ```

### **That's it! 🎉**

Your chatbot is now live and accessible to anyone with the link!

---

## 🔧 **Option B: Frontend on Pages + Backend Elsewhere**

If you want to keep your API key secure:

### **Step 1: Deploy Backend to Railway**

1. Go to https://railway.app
2. Login with GitHub
3. Deploy `jai-llm-chatbot`
4. Add environment variable: `GEMINI_API_KEY`
5. Copy your Railway URL

### **Step 2: Update Frontend**

Edit `rag-deployment/frontend/chat.js` line 3:
```javascript
const API_URL = 'https://your-app.railway.app';
```

### **Step 3: Enable GitHub Pages**

1. Go to repo Settings → Pages
2. Source: `main` branch
3. Folder: `/rag-deployment/frontend`
4. Save

**Your site:** `https://jai-nayani.github.io/jai-llm-chatbot/`

---

## 📊 **Comparison**

| Feature | Serverless (docs/) | Backend + Frontend |
|---------|-------------------|-------------------|
| **Setup Time** | 5 minutes | 15 minutes |
| **Cost** | FREE | FREE |
| **Security** | API key visible | API key hidden |
| **Maintenance** | None | Update backend |
| **Performance** | Fast | Fast |
| **Best For** | Personal projects | Production apps |

---

## ✅ **Post-Deployment Checklist**

After enabling GitHub Pages:

- [ ] Wait 2-3 minutes for site to build
- [ ] Visit your site URL
- [ ] Test the chatbot with a question
- [ ] Verify responses are working
- [ ] Share your live demo link!

---

## 🎨 **Customize Your Deployment**

### **Add Custom Domain:**

1. Buy domain from Namecheap/GoDaddy
2. Go to repo Settings → Pages
3. Add custom domain
4. Update DNS records as shown
5. Enable HTTPS (automatic)

### **Update Resume Info:**

Edit `docs/chat.js` line 7-40 to update the `RESUME_CONTEXT` with your latest information.

---

## 🐛 **Troubleshooting**

### **"Site not found" error:**
- Wait 2-3 minutes after enabling Pages
- Check Settings → Pages to see build status
- Make sure `docs/` folder exists in main branch

### **"API key error":**
- Verify your Gemini API key is correct
- Check API quota hasn't been exceeded
- Try regenerating API key from Google AI Studio

### **Chat not responding:**
- Open browser console (F12)
- Check for errors
- Verify API key is valid
- Check network tab for failed requests

---

## 🔐 **Security Note**

**For the serverless version (docs/):**
- Your API key is visible in the browser code
- This is fine for:
  - Personal projects
  - Portfolios
  - Learning projects
  - Low-traffic demos

**For production apps:**
- Use Option B (backend + frontend)
- Keep API key on server side
- Add rate limiting
- Use authentication

---

## 📈 **Monitor Your Site**

### **GitHub Pages Analytics:**
- Go to repo Insights → Traffic
- See page views and visitors
- Track popular referrers

### **Google Analytics (Optional):**
Add to `docs/index.html` before `</head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

---

## 🎉 **Success!**

Your chatbot is now live on GitHub Pages!

**Share your deployment:**
- Add "Live Demo" badge to README
- Share on LinkedIn/Twitter
- Add to your portfolio
- Show it in job applications

**Your Live URL:**
```
https://jai-nayani.github.io/jai-llm-chatbot/
```

---

## 📚 **Useful Links**

- **GitHub Pages Docs:** https://docs.github.com/pages
- **Custom Domains:** https://docs.github.com/pages/configuring-a-custom-domain
- **Troubleshooting:** https://docs.github.com/pages/getting-started-with-github-pages/troubleshooting-404-errors

---

**Deployed and live in 5 minutes! 🚀**

