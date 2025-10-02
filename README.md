# 💬 Jai LLM - Resume-based Chatbot

An intelligent chatbot built with RAG (Retrieval Augmented Generation) and Google Gemini API that answers questions about Jai Adithya Nayani's professional experience, skills, and background. This project demonstrates both ML engineering (fine-tuning) and practical AI deployment.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Project Overview

This project combines two approaches:

1. **Fine-tuning Pipeline** (Showcasing ML Skills)
   - Fine-tune GPT-2 with LoRA on resume data
   - Complete training pipeline with evaluation
   - Demonstrates ML engineering capabilities

2. **RAG Deployment** (Production Chatbot)
   - Semantic search with ChromaDB
   - Google Gemini API for generation
   - Fast, accurate, and easy to update

## ✨ Features

- 🤖 **Intelligent Q&A**: Natural conversation about professional background
- 🔍 **Semantic Search**: RAG-based context retrieval
- 🚀 **Fast Responses**: Powered by Google Gemini API
- 🎨 **Beautiful UI**: Modern, responsive web interface
- 🔧 **Easy Updates**: No retraining needed to update information
- 💻 **Local Training**: Fine-tune models on your MacBook
- 📊 **Model Evaluation**: Comprehensive testing framework

## 🏗️ Project Structure

```
jai-llm-chatbot/
├── data/                          # Resume data and processing
│   ├── download_resumes.py       # Download PDFs from Google Drive
│   ├── process_data.py           # Process and prepare training data
│   ├── *.pdf                     # Resume PDFs (gitignored)
│   ├── combined_resume.txt       # Processed resume text
│   └── training_data.jsonl       # Training data for fine-tuning
│
├── fine-tuning/                   # ML training pipeline
│   ├── train.py                  # Fine-tune GPT-2 with LoRA
│   ├── evaluate.py               # Test the fine-tuned model
│   └── model_comparison.py       # Compare different approaches
│
├── rag-deployment/                # Production chatbot
│   ├── backend/
│   │   ├── app.py               # FastAPI server
│   │   ├── embeddings.py        # RAG system with ChromaDB
│   │   └── requirements.txt     # Backend dependencies
│   └── frontend/
│       ├── index.html           # Web interface
│       ├── chat.js              # Chat functionality
│       └── styles.css           # Modern styling
│
├── models/                        # Trained models (gitignored)
├── notebooks/                     # Jupyter notebooks for exploration
├── config.py                      # Configuration
├── requirements.txt               # All dependencies
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- MacBook with M1/M2 (or any machine with 8GB+ RAM)
- Google Gemini API key (free tier available)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/jai-nayani/jai-llm-chatbot.git
cd jai-llm-chatbot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download resume data**
```bash
# Manually download PDFs from Google Drive and place in data/ folder
# Or run the download script:
python data/download_resumes.py
```

5. **Process the data**
```bash
python data/process_data.py
```

6. **Configure API keys**
```bash
# Edit config.py with your Gemini API key
# Or create .env file (recommended)
```

## 💡 Usage

### Option 1: RAG Chatbot (Recommended)

**Start the backend:**
```bash
cd rag-deployment/backend
python app.py
```

**Open the frontend:**
```bash
# Open rag-deployment/frontend/index.html in your browser
# Or use a local server:
python -m http.server 8080 --directory rag-deployment/frontend
```

Visit: `http://localhost:8080`

### Option 2: Fine-tuned Model

**Train the model:**
```bash
python fine-tuning/train.py
```

**Test the model:**
```bash
python fine-tuning/evaluate.py
```

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Google Gemini
GEMINI_API_KEY = "your_api_key_here"

# Model settings
TEMPERATURE = 0.7
MAX_TOKENS = 1024

# RAG settings
CHUNK_SIZE = 500
TOP_K_RESULTS = 3

# Fine-tuning settings
LEARNING_RATE = 2e-4
NUM_EPOCHS = 3
```

## 📊 API Documentation

Once the backend is running, visit:
- Interactive API docs: `http://localhost:8000/docs`
- OpenAPI schema: `http://localhost:8000/openapi.json`

### Endpoints

**POST /chat**
```json
{
  "message": "What are your technical skills?",
  "conversation_history": []
}
```

**Response:**
```json
{
  "response": "I have expertise in...",
  "sources": ["relevant context snippets"]
}
```

## 🎨 Frontend Features

- **Modern UI**: Clean, professional design
- **Quick Questions**: Pre-built queries for common questions
- **Typing Indicators**: Visual feedback during processing
- **Responsive Design**: Works on desktop and mobile
- **Conversation History**: Maintains context across messages

## 🧪 Testing

Test the RAG system:
```bash
python rag-deployment/backend/embeddings.py
```

Test the fine-tuned model:
```bash
python fine-tuning/evaluate.py
```

## 📈 Performance

- **Response Time**: < 2 seconds (with Gemini API)
- **Accuracy**: High relevance with RAG context
- **Cost**: Free tier (15 requests/minute)
- **Scalability**: Easily deployable to cloud platforms

## 🚢 Deployment

### Frontend (GitHub Pages)

1. Push to GitHub
2. Enable GitHub Pages in repository settings
3. Select `rag-deployment/frontend` as source

### Backend Options

**Option A: Google Cloud Run** (Recommended)
```bash
gcloud run deploy jai-llm-api --source .
```

**Option B: Railway**
- Connect GitHub repository
- Set environment variables
- Deploy automatically

**Option C: Vercel (Serverless)**
- Deploy as Vercel Functions
- Set environment variables in dashboard

## 🛠️ Technology Stack

- **ML Framework**: PyTorch, Transformers, PEFT (LoRA)
- **LLM**: Google Gemini Pro
- **Vector DB**: ChromaDB
- **Embeddings**: Sentence Transformers
- **Backend**: FastAPI
- **Frontend**: Vanilla JavaScript (no frameworks)
- **Styling**: Modern CSS with animations

## 📝 Example Questions

Try asking:
- "What are your main technical skills?"
- "Tell me about your experience with machine learning"
- "What projects have you worked on?"
- "Which programming languages do you know?"
- "What cloud platforms are you familiar with?"

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini for the powerful API
- HuggingFace for transformer models
- FastAPI for the excellent web framework
- ChromaDB for vector storage

## 📧 Contact

**Jai Adithya Nayani**
- Portfolio: [jai-nayani.github.io](https://jai-nayani.github.io/)
- GitHub: [@jai-nayani](https://github.com/jai-nayani)

---

⭐ Star this repo if you find it helpful!

Built with ❤️ and ☕

