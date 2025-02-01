import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"  # Use an open-source LLM if you intend to like Meta, DeepSeek, Mistral, Falcon etc.  

def train():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to("cuda")

    dataset = load_dataset("data/bharatwasi_dataset.csv")

    training_args = TrainingArguments(
        output_dir="./models/BharatwASI_v1",
        per_device_train_batch_size=2,
        save_steps=10_000,
        save_total_limit=2,
        num_train_epochs=3,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
    )

    trainer.train()
    model.save_pretrained("./models/BharatwASI_v1")
    tokenizer.save_pretrained("./models/BharatwASI_v1")

if __name__ == "__main__":
    train()
