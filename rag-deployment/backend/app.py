"""
FastAPI backend for Jai's Resume Chatbot using RAG with Google Gemini
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from typing import List, Optional
import sys
sys.path.append('../..')
from config import *
from embeddings import ResumeRAG

# Initialize FastAPI app
app = FastAPI(
    title="Jai LLM Chatbot API",
    description="Resume-based chatbot using RAG with Google Gemini",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# Initialize RAG system
rag_system = None


class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[dict]] = []


class ChatResponse(BaseModel):
    response: str
    sources: Optional[List[str]] = []


@app.on_event("startup")
async def startup_event():
    """Initialize RAG system on startup"""
    global rag_system
    print("🚀 Initializing RAG system...")
    try:
        rag_system = ResumeRAG(data_dir="../../data")
        print("✅ RAG system initialized!")
    except Exception as e:
        print(f"⚠️  Warning: Could not initialize RAG system: {e}")
        print("The chatbot will work but without resume context.")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "service": "Jai LLM Chatbot API",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "gemini_configured": bool(GEMINI_API_KEY),
        "rag_initialized": rag_system is not None
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint"""
    try:
        user_message = request.message.strip()
        
        if not user_message:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Get relevant context from RAG
        relevant_chunks = []
        if rag_system:
            relevant_chunks = rag_system.query(user_message, top_k=TOP_K_RESULTS)
        
        # Build context
        context = ""
        if relevant_chunks:
            context = "Based on Jai's resume:\n\n"
            context += "\n\n".join([chunk["text"] for chunk in relevant_chunks])
            context += "\n\n"
        
        # Build prompt
        system_prompt = """You are a helpful assistant answering questions about Jai Adithya Nayani based on his resume. 
Be professional, concise, and friendly. If you don't have specific information, provide a helpful general answer.
Speak in first person as if you are Jai when answering about his experience and background."""
        
        full_prompt = f"""{system_prompt}

{context}Question: {user_message}

Answer:"""
        
        # Generate response with Gemini
        response = model.generate_content(
            full_prompt,
            generation_config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_TOKENS,
            }
        )
        
        return ChatResponse(
            response=response.text,
            sources=[chunk["text"][:100] + "..." for chunk in relevant_chunks[:2]]
        )
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/reset")
async def reset_conversation():
    """Reset conversation history"""
    return {"status": "conversation reset"}


if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Jai LLM Chatbot API...")
    print(f"📍 Server will run at: http://localhost:8000")
    print(f"📚 API docs at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)

