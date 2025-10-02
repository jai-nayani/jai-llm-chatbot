"""
Quick start script to test the chatbot locally
"""

import subprocess
import sys
import time
import webbrowser
from pathlib import Path


def check_dependencies():
    """Check if required packages are installed"""
    print("🔍 Checking dependencies...")
    
    try:
        import google.generativeai
        import chromadb
        import fastapi
        print("✅ All dependencies installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\nPlease run: pip install -r requirements.txt")
        return False


def check_data():
    """Check if data is processed"""
    print("\n🔍 Checking data...")
    
    data_file = Path("data/processed_data.json")
    if data_file.exists():
        print("✅ Data processed")
        return True
    else:
        print("⚠️  Data not processed yet")
        print("\nPlease run: python data/process_data.py")
        return False


def start_backend():
    """Start the FastAPI backend"""
    print("\n🚀 Starting backend server...")
    
    backend_script = Path("rag-deployment/backend/app.py")
    
    if not backend_script.exists():
        print("❌ Backend script not found")
        return None
    
    # Start backend in subprocess
    process = subprocess.Popen(
        [sys.executable, str(backend_script)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    
    if process.poll() is None:
        print("✅ Backend running on http://localhost:8000")
        return process
    else:
        print("❌ Failed to start backend")
        return None


def open_frontend():
    """Open the frontend in browser"""
    print("\n🌐 Opening frontend...")
    
    frontend_file = Path("rag-deployment/frontend/index.html")
    
    if not frontend_file.exists():
        print("❌ Frontend not found")
        return False
    
    # Open in browser
    webbrowser.open(f"file://{frontend_file.absolute()}")
    print("✅ Frontend opened in browser")
    
    return True


def main():
    """Main quick start function"""
    print("="*60)
    print("  🤖 Jai LLM Chatbot - Quick Start")
    print("="*60)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check data
    if not check_data():
        response = input("\nWould you like to process data now? (y/n): ")
        if response.lower() == 'y':
            print("\n📊 Processing data...")
            subprocess.run([sys.executable, "data/process_data.py"])
        else:
            print("\nPlease process data first: python data/process_data.py")
            return
    
    # Start backend
    backend_process = start_backend()
    
    if backend_process is None:
        return
    
    # Open frontend
    open_frontend()
    
    print("\n" + "="*60)
    print("  ✨ Setup Complete!")
    print("="*60)
    print("\n📍 Backend: http://localhost:8000")
    print("📍 API Docs: http://localhost:8000/docs")
    print("📍 Frontend: Opened in browser")
    print("\nℹ️  For better experience, start a local server:")
    print("   python -m http.server 8080 --directory rag-deployment/frontend")
    print("\n⚠️  Press Ctrl+C to stop the backend server")
    
    try:
        # Keep running until interrupted
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        backend_process.terminate()
        print("✅ Backend stopped")


if __name__ == "__main__":
    main()

