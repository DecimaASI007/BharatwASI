from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import BharatwASI

app = FastAPI()
chatbot = BharatwASI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot.chat(request.message)
    return {"response": response}

# Run using: uvicorn api:app --host 0.0.0.0 --port 8000
