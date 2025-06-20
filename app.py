from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot import stream_graph_updates

app = FastAPI()

# Allow CORS for all origins

@app.get("/")
def root():
    return {"message": "API is running!"}

from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = stream_graph_updates(request.user_input)
    return {"response": response}


