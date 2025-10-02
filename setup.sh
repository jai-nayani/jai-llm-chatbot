#!/bin/bash

# Setup script for Jai LLM Chatbot

echo "🚀 Setting up Jai LLM Chatbot..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p models data/raw chroma_db logs

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your API keys!"
fi

echo ""
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Download your resume PDFs and place them in the data/ folder"
echo "2. Run: python data/process_data.py"
echo "3. Start backend: python rag-deployment/backend/app.py"
echo "4. Open rag-deployment/frontend/index.html in your browser"
echo ""
echo "For fine-tuning: python fine-tuning/train.py"
echo ""
echo "Happy coding! 🎉"

