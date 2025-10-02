"""
Fine-tune GPT-2 using LoRA on resume data
This demonstrates ML engineering skills for GitHub portfolio
"""

import json
import torch
from pathlib import Path
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import sys
sys.path.append('..')
from config import *


def load_training_data(data_path: str) -> Dataset:
    """Load and prepare training data"""
    data = []
    with open(data_path, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            # Format as conversation
            text = f"Question: {item['instruction']}\nAnswer: {item['output']}"
            data.append({"text": text})
    
    return Dataset.from_list(data)


def tokenize_function(examples, tokenizer, max_length=512):
    """Tokenize the dataset"""
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=max_length,
        padding="max_length"
    )


def train_model():
    """Main training function"""
    print("🚀 Starting fine-tuning process...")
    
    # Check device
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")
    
    # Load tokenizer and model
    print(f"\n📥 Loading {FINE_TUNE_MODEL}...")
    tokenizer = AutoTokenizer.from_pretrained(FINE_TUNE_MODEL)
    
    # Add pad token if not present
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    model = AutoModelForCausalLM.from_pretrained(
        FINE_TUNE_MODEL,
        torch_dtype=torch.float32,  # Use float32 for MPS
        device_map={"": device}
    )
    
    # Configure LoRA
    print("\n⚙️  Configuring LoRA...")
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        target_modules=["c_attn"],  # GPT-2 attention modules
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    # Load training data
    print("\n📊 Loading training data...")
    data_path = Path("../data/training_data.jsonl")
    
    if not data_path.exists():
        print("❌ Training data not found!")
        print("Please run: python data/process_data.py")
        return
    
    dataset = load_training_data(data_path)
    print(f"Loaded {len(dataset)} training examples")
    
    # Tokenize dataset
    print("\n🔤 Tokenizing dataset...")
    tokenized_dataset = dataset.map(
        lambda x: tokenize_function(x, tokenizer),
        batched=True,
        remove_columns=dataset.column_names
    )
    
    # Split into train/eval
    split_dataset = tokenized_dataset.train_test_split(test_size=0.1)
    
    # Training arguments
    output_dir = Path("../models/gpt2-jai-resume-lora")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    training_args = TrainingArguments(
        output_dir=str(output_dir),
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        learning_rate=LEARNING_RATE,
        logging_steps=10,
        eval_strategy="steps",
        eval_steps=50,
        save_steps=100,
        warmup_steps=50,
        fp16=False,  # Don't use fp16 on MPS
        report_to="none",
        load_best_model_at_end=True,
    )
    
    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )
    
    # Initialize trainer
    print("\n🏋️  Initializing trainer...")
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=split_dataset["train"],
        eval_dataset=split_dataset["test"],
        data_collator=data_collator,
    )
    
    # Train!
    print("\n🔥 Starting training...\n")
    trainer.train()
    
    # Save model
    print("\n💾 Saving model...")
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    
    print(f"\n✅ Training complete! Model saved to: {output_dir}")
    print("\nTo test the model, run: python fine-tuning/evaluate.py")


if __name__ == "__main__":
    train_model()

