import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import Config

class BharatwASI:
    def __init__(self, model_path=Config.MODEL_PATH):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path).to(Config.DEVICE)

    def chat(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(Config.DEVICE)
        outputs = self.model.generate(**inputs, max_length=Config.CONTEXT_LENGTH)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    bot = BharatwASI()
    response = bot.chat("Namaste, how are you?")
    print(response)
