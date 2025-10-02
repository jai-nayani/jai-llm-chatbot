"""
Process resume PDFs into structured data for fine-tuning and RAG
"""

import json
import re
from pathlib import Path
from typing import List, Dict
import PyPDF2


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text content from PDF"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text


def clean_text(text: str) -> str:
    """Clean and normalize extracted text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep important punctuation
    text = re.sub(r'[^\w\s.,;:()\-@]', '', text)
    return text.strip()


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks"""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return chunks


def create_qa_pairs() -> List[Dict[str, str]]:
    """Create Q&A pairs for fine-tuning"""
    qa_pairs = [
        {
            "question": "Who are you?",
            "answer": "I'm Jai Adithya Nayani, a software engineer specializing in AI/ML and full-stack development."
        },
        {
            "question": "What is your educational background?",
            "answer": "I'm currently pursuing my Master's degree with a focus on Computer Science and AI/ML technologies."
        },
        {
            "question": "What are your main technical skills?",
            "answer": "I have expertise in Python, Java, C++, machine learning frameworks like TensorFlow and PyTorch, cloud platforms (AWS, GCP), and full-stack web development."
        },
        {
            "question": "What kind of projects have you worked on?",
            "answer": "I've worked on various projects including machine learning models, computer vision applications, web applications, and data engineering pipelines."
        },
        {
            "question": "What programming languages do you know?",
            "answer": "I'm proficient in Python, Java, C++, JavaScript, and have experience with SQL and other languages."
        },
        {
            "question": "Do you have any experience with cloud platforms?",
            "answer": "Yes, I have hands-on experience with AWS and Google Cloud Platform for deploying and scaling applications."
        },
        {
            "question": "What ML frameworks are you familiar with?",
            "answer": "I work extensively with TensorFlow, PyTorch, scikit-learn, and Keras for building and deploying machine learning models."
        },
        {
            "question": "What's your approach to problem-solving?",
            "answer": "I approach problems systematically by first understanding requirements, breaking down complex tasks, implementing solutions iteratively, and optimizing for performance and scalability."
        },
        {
            "question": "Tell me about your experience with AI/ML",
            "answer": "I have experience building and deploying machine learning models, working with neural networks, computer vision, NLP, and implementing end-to-end ML pipelines."
        },
        {
            "question": "What interests you most in technology?",
            "answer": "I'm passionate about artificial intelligence, machine learning, and building scalable systems that solve real-world problems."
        }
    ]
    return qa_pairs


def create_training_data(resume_texts: List[str], qa_pairs: List[Dict]) -> List[Dict]:
    """Create training data in instruction format"""
    training_data = []
    
    # Add Q&A pairs
    for qa in qa_pairs:
        training_data.append({
            "instruction": qa["question"],
            "input": "",
            "output": qa["answer"]
        })
    
    # Add resume context
    for i, text in enumerate(resume_texts):
        chunks = chunk_text(text, chunk_size=300)
        for chunk in chunks:
            training_data.append({
                "instruction": "Tell me about your background and experience.",
                "input": "",
                "output": chunk
            })
    
    return training_data


def main():
    """Main processing pipeline"""
    data_dir = Path(__file__).parent
    output_dir = data_dir
    
    print("Processing resumes...")
    
    # Find all PDF files
    pdf_files = list(data_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("⚠️  No PDF files found. Please download resumes first!")
        print("Run: python data/download_resumes.py")
        return
    
    # Extract text from all resumes
    all_texts = []
    combined_text = ""
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        text = extract_text_from_pdf(pdf_file)
        cleaned = clean_text(text)
        all_texts.append(cleaned)
        combined_text += cleaned + "\n\n"
    
    # Save combined resume text
    with open(output_dir / "combined_resume.txt", 'w', encoding='utf-8') as f:
        f.write(combined_text)
    print(f"✅ Saved combined resume text")
    
    # Create Q&A pairs
    qa_pairs = create_qa_pairs()
    
    # Create training data
    training_data = create_training_data(all_texts, qa_pairs)
    
    # Save in different formats
    
    # 1. JSONL format for fine-tuning
    with open(output_dir / "training_data.jsonl", 'w', encoding='utf-8') as f:
        for item in training_data:
            f.write(json.dumps(item) + '\n')
    print(f"✅ Saved {len(training_data)} training examples to training_data.jsonl")
    
    # 2. JSON format
    with open(output_dir / "processed_data.json", 'w', encoding='utf-8') as f:
        json.dump({
            "qa_pairs": qa_pairs,
            "resume_chunks": chunk_text(combined_text),
            "training_data": training_data
        }, f, indent=2)
    print(f"✅ Saved processed data to processed_data.json")
    
    print("\n✨ Data processing complete!")
    print(f"Total training examples: {len(training_data)}")
    print(f"Total Q&A pairs: {len(qa_pairs)}")


if __name__ == "__main__":
    main()

