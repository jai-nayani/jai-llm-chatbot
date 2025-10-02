"""
Evaluate and test the fine-tuned model
"""

import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


def load_model(base_model="gpt2", adapter_path="../models/gpt2-jai-resume-lora"):
    """Load the fine-tuned model"""
    print("Loading model...")
    
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.float32,
        device_map={"": device}
    )
    
    # Load LoRA adapters
    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()
    
    return model, tokenizer, device


def generate_response(model, tokenizer, device, prompt, max_length=150):
    """Generate response from the model"""
    input_text = f"Question: {prompt}\nAnswer:"
    
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract only the answer part
    if "Answer:" in response:
        response = response.split("Answer:")[-1].strip()
    
    return response


def main():
    """Test the fine-tuned model"""
    adapter_path = Path("../models/gpt2-jai-resume-lora")
    
    if not adapter_path.exists():
        print("❌ Model not found!")
        print("Please train the model first: python fine-tuning/train.py")
        return
    
    model, tokenizer, device = load_model(adapter_path=str(adapter_path))
    
    print("\n✅ Model loaded successfully!")
    print("\n" + "="*60)
    print("Testing Fine-tuned Model - Jai's Resume Chatbot")
    print("="*60)
    
    # Test questions
    test_questions = [
        "Who are you?",
        "What are your main technical skills?",
        "Tell me about your experience",
        "What programming languages do you know?",
        "What interests you in technology?"
    ]
    
    for question in test_questions:
        print(f"\n❓ Q: {question}")
        response = generate_response(model, tokenizer, device, question)
        print(f"💬 A: {response}")
        print("-" * 60)
    
    # Interactive mode
    print("\n\n🎮 Interactive Mode (type 'quit' to exit)")
    print("-" * 60)
    
    while True:
        question = input("\n❓ Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not question:
            continue
        
        response = generate_response(model, tokenizer, device, question)
        print(f"💬 Answer: {response}")


if __name__ == "__main__":
    main()

