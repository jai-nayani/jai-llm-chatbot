# 🚀 Deployment Guide - Jai LLM Chatbot

Complete guide to deploy your chatbot to production for **FREE**.

---

## 📋 **Pre-Deployment Checklist**

Before deploying, make sure:
- ✅ Code is pushed to GitHub
- ✅ Google Gemini API key is ready
- ✅ You've tested the app locally
- ✅ Resume data is processed

---

## 🎯 **Option 1: Vercel + Railway (Recommended)**

**Best for:** Quick deployment, easy setup  
**Cost:** FREE  
**Time:** 15 minutes

### **Step 1: Deploy Backend to Railway**

1. **Go to Railway:**
   - Visit: https://railway.app
   - Sign in with GitHub

2. **Create New Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `jai-llm-chatbot`

3. **Configure Settings:**
   - **Root Directory:** Leave blank
   - **Start Command:** `cd rag-deployment/backend && python app.py`
   - **Install Command:** `pip install -r requirements.txt`

4. **Add Environment Variables:**
   ```
   GEMINI_API_KEY=AIzaSyBP3x80wwVGfoCjNJoy01QrKsaaTzCAkgI
   PORT=8000
   ```

5. **Deploy:**
   - Click "Deploy"
   - Wait for deployment (2-3 minutes)
   - Copy your Railway URL (e.g., `https://your-app.railway.app`)

### **Step 2: Deploy Frontend to Vercel**

1. **Go to Vercel:**
   - Visit: https://vercel.com
   - Sign in with GitHub

2. **Import Project:**
   - Click "Add New" → "Project"
   - Import `jai-llm-chatbot`

3. **Configure:**
   - **Framework Preset:** Other
   - **Root Directory:** `rag-deployment/frontend`
   - **Build Command:** (leave empty)
   - **Output Directory:** `.`

4. **Update Frontend API URL:**
   - Before deploying, update `rag-deployment/frontend/chat.js`
   - Change `API_URL` to your Railway backend URL

5. **Deploy:**
   - Click "Deploy"
   - Your frontend will be live at `https://your-app.vercel.app`

---

## 🌐 **Option 2: All-in-One with Render**

**Best for:** Simplest single-platform solution  
**Cost:** FREE  
**Time:** 10 minutes

### **Deploy Backend:**

1. **Go to Render:**
   - Visit: https://render.com
   - Sign in with GitHub

2. **New Web Service:**
   - Click "New +" → "Web Service"
   - Connect `jai-llm-chatbot` repo

3. **Configure:**
   ```
   Name: jai-llm-backend
   Region: Pick closest to you
   Branch: main
   Root Directory: rag-deployment/backend
   Runtime: Python 3
   Build Command: pip install -r ../../requirements.txt
   Start Command: python app.py
   ```

4. **Environment Variables:**
   ```
   GEMINI_API_KEY=AIzaSyBP3x80wwVGfoCjNJoy01QrKsaaTzCAkgI
   PYTHON_VERSION=3.11
   ```

5. **Deploy:**
   - Click "Create Web Service"
   - Copy your Render URL

### **Deploy Frontend:**

1. **New Static Site:**
   - Click "New +" → "Static Site"
   - Connect same repo

2. **Configure:**
   ```
   Name: jai-llm-frontend
   Branch: main
   Root Directory: rag-deployment/frontend
   Build Command: (leave empty)
   Publish Directory: .
   ```

3. **Update API URL:**
   - Update `chat.js` with backend URL
   - Commit and push changes

---

## ☁️ **Option 3: Google Cloud Run (Most Scalable)**

**Best for:** Production-grade deployment  
**Cost:** FREE tier (2M requests/month)  
**Time:** 20 minutes

### **Deploy Backend:**

1. **Install Google Cloud CLI:**
   ```bash
   brew install google-cloud-sdk
   ```

2. **Login and Setup:**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

3. **Create Dockerfile:**
   Already created at `rag-deployment/backend/Dockerfile`

4. **Deploy:**
   ```bash
   cd rag-deployment/backend
   
   gcloud run deploy jai-llm-backend \
     --source . \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GEMINI_API_KEY=YOUR_KEY
   ```

5. **Get URL:**
   - Copy the Cloud Run URL provided

### **Deploy Frontend:**

Use Vercel or Netlify (as described above) and update API URL.

---

## 📱 **Option 4: GitHub Pages (Frontend Only)**

**Best for:** Static frontend hosting  
**Cost:** FREE  
**Note:** You'll need backend hosted elsewhere

### **Setup:**

1. **Update chat.js:**
   - Change API_URL to your backend URL (Railway/Render)

2. **Enable GitHub Pages:**
   - Go to repo Settings → Pages
   - Source: Deploy from branch
   - Branch: `main`
   - Folder: `/rag-deployment/frontend`
   - Save

3. **Access:**
   - Your site will be live at: `https://jai-nayani.github.io/jai-llm-chatbot/`

---

## 🔧 **Update Frontend API URL**

After deploying backend, update the frontend:

**File:** `rag-deployment/frontend/chat.js`

```javascript
// Line 3 - Change this:
const API_URL = 'http://localhost:8000';

// To your deployed backend URL:
const API_URL = 'https://your-backend.railway.app';
```

Then commit and push:
```bash
git add rag-deployment/frontend/chat.js
git commit -m "Update API URL for production"
git push
```

---

## 🎨 **Custom Domain (Optional)**

### **Vercel:**
1. Go to Project Settings → Domains
2. Add your custom domain
3. Update DNS records as shown

### **Railway:**
1. Go to Settings → Domains
2. Generate domain or add custom domain

---

## 🔐 **Security Best Practices**

1. **Environment Variables:**
   - Never commit API keys
   - Use platform's secret management

2. **CORS Configuration:**
   - Update `app.py` with your frontend URL
   ```python
   allow_origins=["https://your-frontend.vercel.app"]
   ```

3. **Rate Limiting:**
   - Add rate limiting to prevent abuse
   - Use Railway/Render built-in protection

---

## 📊 **Monitor Your Deployment**

### **Railway:**
- Dashboard shows logs, metrics, and usage
- Free tier: 500 hours/month

### **Vercel:**
- Analytics tab shows page views and performance
- Free tier: Unlimited bandwidth

### **Render:**
- Logs tab for debugging
- Free tier: 750 hours/month

---

## 🐛 **Troubleshooting**

### **"Module not found" error:**
```bash
# Make sure requirements.txt includes all dependencies
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### **CORS errors:**
```python
# In app.py, update CORS origins:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.vercel.app"],
    ...
)
```

### **API timeout:**
```python
# Increase timeout in deployment settings
# Railway: Settings → Timeout → 300s
# Render: Advanced → Timeout → 300s
```

### **Cold starts:**
- Free tiers sleep after inactivity
- First request may take 5-10 seconds
- Use a service like UptimeRobot to keep it awake

---

## 📈 **Performance Tips**

1. **Enable Caching:**
   - Cache embeddings for faster responses
   - Use Redis for session storage

2. **Optimize API Calls:**
   - Reduce chunk size if responses are slow
   - Adjust `TOP_K_RESULTS` in config

3. **CDN for Frontend:**
   - Vercel includes CDN automatically
   - Faster global loading times

---

## 💰 **Cost Breakdown**

| Service | Free Tier | Limit |
|---------|-----------|-------|
| **Railway** | FREE | 500 hours/month |
| **Vercel** | FREE | Unlimited bandwidth |
| **Render** | FREE | 750 hours/month |
| **Google Cloud Run** | FREE | 2M requests/month |
| **Gemini API** | FREE | 15 requests/minute |
| **Total** | **$0/month** | Plenty for personal use |

---

## 🚀 **Quick Deploy Commands**

### **Railway (via CLI):**
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

### **Vercel (via CLI):**
```bash
npm i -g vercel
vercel login
vercel
```

### **Render (via CLI):**
```bash
# Use web dashboard - no CLI needed
```

---

## ✅ **Post-Deployment Checklist**

After deployment:
- [ ] Backend is accessible and returns 200
- [ ] Frontend loads without errors
- [ ] Can send chat messages successfully
- [ ] Responses are relevant and accurate
- [ ] No CORS errors in browser console
- [ ] API key is secure (not in code)
- [ ] Custom domain configured (optional)
- [ ] Monitoring/analytics set up
- [ ] Shared URL with friends to test
- [ ] Updated portfolio with live link

---

## 🎉 **Success!**

Your chatbot is now live and accessible worldwide!

**Share your deployment:**
- Add live demo link to README
- Update portfolio with live demo
- Share on LinkedIn/Twitter
- Show it in job applications

---

## 📞 **Need Help?**

- **Railway Docs:** https://docs.railway.app
- **Vercel Docs:** https://vercel.com/docs
- **Render Docs:** https://render.com/docs
- **FastAPI Deployment:** https://fastapi.tiangolo.com/deployment/

---

**Built with ❤️ | Now deployed and live! 🚀**

