import torch
import logging
import json
from transformers import AutoTokenizer, AutoModelForCausalLM

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_model(model_name="deepseek-ai/DeepSeek-R1", device="cuda" if torch.cuda.is_available() else "cpu"):
    """
    Load the DeepSeek-R1 model and tokenizer.
    """
    logging.info(f"Loading model: {model_name} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
    return tokenizer, model

def preprocess_text(text):
    """
    Preprocess input text: trim and normalize.
    """
    return text.strip()

def generate_response(model, tokenizer, prompt, max_length=1024, device="cuda" if torch.cuda.is_available() else "cpu"):
    """
    Generate a response from the AI model given a prompt.
    """
    logging.info("Generating response...")
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_length=max_length)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def save_json(data, filename="output.json"):
    """
    Save dictionary data to a JSON file.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"Data saved to {filename}")

def load_json(filename="output.json"):
    """
    Load JSON data from a file.
    """
    with open(filename, "r") as f:
        return json.load(f)

def check_cuda():
    """
    Check if CUDA is available and return the device.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logging.info(f"Using device: {device}")
    return device
