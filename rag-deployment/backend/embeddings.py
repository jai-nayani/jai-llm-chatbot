"""
RAG system using ChromaDB for semantic search over resume data
"""

import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
import json
from typing import List, Dict
import sys
sys.path.append('../..')
from config import *


class ResumeRAG:
    """RAG system for resume-based Q&A"""
    
    def __init__(self, data_dir: str = "../../data"):
        """Initialize RAG system"""
        self.data_dir = Path(data_dir)
        
        # Initialize ChromaDB
        self.client = chromadb.Client()
        
        # Use sentence transformers for embeddings
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="jai_resume",
            embedding_function=self.embedding_fn
        )
        
        # Load resume data
        self._load_resume_data()
    
    def _load_resume_data(self):
        """Load and index resume data"""
        processed_data_path = self.data_dir / "processed_data.json"
        
        if not processed_data_path.exists():
            print("⚠️  Processed data not found. Using default data.")
            self._create_default_data()
            return
        
        print(f"📥 Loading resume data from {processed_data_path}")
        
        with open(processed_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if collection is empty
        if self.collection.count() > 0:
            print(f"✅ Collection already has {self.collection.count()} documents")
            return
        
        # Add resume chunks
        chunks = data.get("resume_chunks", [])
        qa_pairs = data.get("qa_pairs", [])
        
        documents = []
        metadatas = []
        ids = []
        
        # Add resume chunks
        for i, chunk in enumerate(chunks):
            documents.append(chunk)
            metadatas.append({"type": "resume_chunk", "index": i})
            ids.append(f"chunk_{i}")
        
        # Add Q&A pairs
        for i, qa in enumerate(qa_pairs):
            # Add both question and answer for better retrieval
            text = f"Q: {qa['question']}\nA: {qa['answer']}"
            documents.append(text)
            metadatas.append({"type": "qa_pair", "index": i})
            ids.append(f"qa_{i}")
        
        # Add to collection
        if documents:
            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"✅ Indexed {len(documents)} documents")
    
    def _create_default_data(self):
        """Create default data if no processed data exists"""
        default_data = [
            "Jai Adithya Nayani is a software engineer specializing in AI/ML and full-stack development.",
            "Proficient in Python, Java, C++, JavaScript with expertise in machine learning frameworks.",
            "Experience with TensorFlow, PyTorch, scikit-learn for building ML models.",
            "Skilled in cloud platforms including AWS and Google Cloud Platform.",
            "Strong background in computer vision, NLP, and data engineering.",
            "Passionate about building scalable AI systems and solving real-world problems."
        ]
        
        self.collection.add(
            documents=default_data,
            metadatas=[{"type": "default", "index": i} for i in range(len(default_data))],
            ids=[f"default_{i}" for i in range(len(default_data))]
        )
        print(f"✅ Created default knowledge base with {len(default_data)} documents")
    
    def query(self, query_text: str, top_k: int = 3) -> List[Dict]:
        """Query the knowledge base"""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=top_k
        )
        
        # Format results
        formatted_results = []
        if results and results['documents']:
            for i, doc in enumerate(results['documents'][0]):
                formatted_results.append({
                    "text": doc,
                    "metadata": results['metadatas'][0][i],
                    "distance": results['distances'][0][i] if 'distances' in results else None
                })
        
        return formatted_results
    
    def add_document(self, text: str, metadata: Dict = None):
        """Add a new document to the knowledge base"""
        doc_id = f"custom_{self.collection.count()}"
        self.collection.add(
            documents=[text],
            metadatas=[metadata or {"type": "custom"}],
            ids=[doc_id]
        )


# Test the RAG system
if __name__ == "__main__":
    print("🧪 Testing RAG system...")
    
    rag = ResumeRAG()
    
    test_queries = [
        "What are Jai's technical skills?",
        "Tell me about his experience",
        "What programming languages does he know?"
    ]
    
    for query in test_queries:
        print(f"\n❓ Query: {query}")
        results = rag.query(query, top_k=2)
        
        for i, result in enumerate(results):
            print(f"\n  Result {i+1}:")
            print(f"  {result['text'][:150]}...")
            print(f"  Distance: {result['distance']:.3f}" if result['distance'] else "")

