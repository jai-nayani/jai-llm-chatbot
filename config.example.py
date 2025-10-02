"""
Configuration file for Jai LLM Chatbot
INSTRUCTIONS:
1. Copy this file to config.py
2. Add your actual API keys
3. Never commit config.py to git
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Google Gemini API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
GEMINI_PROJECT_NAME = os.getenv("GEMINI_PROJECT_NAME", "projects/YOUR_PROJECT_NUMBER")
GEMINI_PROJECT_NUMBER = os.getenv("GEMINI_PROJECT_NUMBER", "YOUR_PROJECT_NUMBER")

# Model Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-pro")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))

# RAG Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", "3"))

# Paths
DATA_DIR = "data"
MODELS_DIR = "models"
CHROMA_DB_DIR = "chroma_db"

# Fine-tuning Configuration
FINE_TUNE_MODEL = "gpt2"  # or "microsoft/phi-2"
LEARNING_RATE = 2e-4
BATCH_SIZE = 4
NUM_EPOCHS = 3
LORA_R = 8
LORA_ALPHA = 16
LORA_DROPOUT = 0.05

