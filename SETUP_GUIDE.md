# 🚀 Complete Setup Guide

This guide will walk you through setting up the Jai LLM Chatbot from scratch.

## 📋 Prerequisites

Before you begin, ensure you have:

- ✅ Python 3.9 or higher installed
- ✅ Git installed
- ✅ 8GB+ RAM (16GB recommended)
- ✅ Google Gemini API key ([Get one here](https://ai.google.dev/))
- ✅ Your resume PDFs ready

## 🎯 Step-by-Step Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/jai-nayani/jai-llm-chatbot.git
cd jai-llm-chatbot
```

### Step 2: Run Setup Script (macOS/Linux)

```bash
chmod +x setup.sh
./setup.sh
```

Or manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure API Keys

Edit `config.py` or create `.env`:

```bash
# Create .env file
cp .env.example .env

# Edit with your favorite editor
nano .env  # or vim, or code
```

Add your Gemini API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 4: Prepare Resume Data

#### Option A: Manual Download
1. Go to your Google Drive folder
2. Download all resume PDFs
3. Place them in the `data/` directory

#### Option B: Use Script (if you have file IDs)
```bash
python data/download_resumes.py
```

### Step 5: Process the Data

```bash
python data/process_data.py
```

This will:
- Extract text from PDFs
- Create training data
- Prepare chunks for RAG
- Save processed files

Expected output:
```
Processing resumes...
Processing: JaiNayani_SDE.pdf
✅ Saved combined resume text
✅ Saved 50 training examples to training_data.jsonl
✅ Saved processed data to processed_data.json
```

### Step 6: Choose Your Path

#### 🎯 Path A: Deploy RAG Chatbot (Recommended First)

**Terminal 1 - Start Backend:**
```bash
cd rag-deployment/backend
python app.py
```

Expected output:
```
🚀 Starting Jai LLM Chatbot API...
📍 Server will run at: http://localhost:8000
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Terminal 2 - Start Frontend:**
```bash
# Option 1: Direct open
open rag-deployment/frontend/index.html

# Option 2: Local server (better for CORS)
cd rag-deployment/frontend
python -m http.server 8080
```

Visit: `http://localhost:8080`

#### 🧠 Path B: Fine-tune Model (For GitHub Showcase)

```bash
python fine-tuning/train.py
```

This will:
- Load GPT-2 model
- Apply LoRA adapters
- Train on your resume data
- Save the model

Training time: ~10-20 minutes on M2 MacBook

Test the model:
```bash
python fine-tuning/evaluate.py
```

## ✅ Verification

### Test Backend API

```bash
# Health check
curl http://localhost:8000/health

# Test chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What are your skills?"}'
```

### Test Frontend

1. Open `http://localhost:8080`
2. Try a quick question button
3. Type a custom question
4. Verify responses appear

## 🐛 Troubleshooting

### Issue: "No PDF files found"

**Solution:**
```bash
# Check if PDFs are in data/
ls data/*.pdf

# If not, download them manually
# Place all resume PDFs in data/ directory
```

### Issue: "Gemini API Error"

**Solution:**
```bash
# Verify API key is correct
cat config.py | grep GEMINI_API_KEY

# Test API key
python -c "import google.generativeai as genai; genai.configure(api_key='YOUR_KEY'); print('API key works!')"
```

### Issue: "Port already in use"

**Solution:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>

# Or use different port
uvicorn app:app --port 8001
```

### Issue: "Module not found"

**Solution:**
```bash
# Ensure virtual environment is activated
which python  # Should show path in venv/

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: "CORS error in browser"

**Solution:**
```bash
# Use local server instead of file://
cd rag-deployment/frontend
python -m http.server 8080

# Or update CORS settings in backend/app.py
```

### Issue: "Model training too slow"

**Solution:**
```python
# In config.py, reduce these values:
BATCH_SIZE = 2  # Instead of 4
NUM_EPOCHS = 2  # Instead of 3
```

## 📊 Project Structure After Setup

```
jai-llm-chatbot/
├── venv/                    ✅ Virtual environment
├── data/
│   ├── *.pdf               ✅ Your resume PDFs
│   ├── combined_resume.txt ✅ Processed text
│   └── training_data.jsonl ✅ Training data
├── models/                 ✅ (After training)
│   └── gpt2-jai-resume-lora/
├── chroma_db/              ✅ Vector database
└── .env                    ✅ Your API keys
```

## 🎓 Learning Resources

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [LoRA Paper](https://arxiv.org/abs/2106.09685)
- [RAG Explanation](https://arxiv.org/abs/2005.11401)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)

## 🚢 Next Steps

1. ✅ Test the chatbot thoroughly
2. ✅ Customize the frontend styling
3. ✅ Add more Q&A pairs in `data/process_data.py`
4. ✅ Train the fine-tuned model
5. ✅ Deploy to production
6. ✅ Push to GitHub

## 📞 Need Help?

- Check the main [README.md](README.md)
- Open an issue on GitHub
- Review the code comments

## 🎉 Success Checklist

- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] API key configured
- [ ] Resume PDFs added
- [ ] Data processed successfully
- [ ] Backend running on port 8000
- [ ] Frontend accessible in browser
- [ ] Can chat with the bot
- [ ] Responses are relevant

---

**Congratulations! Your chatbot is ready! 🎊**

Now test it with various questions and deploy it to share with the world!

