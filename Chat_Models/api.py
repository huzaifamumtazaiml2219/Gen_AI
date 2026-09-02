from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = ChatOpenAI(model="gpt-4.1", temperature=0)

modes = {
    "1": "You are an angry agent. You respond aggressively and impatiently.",
    "2": "You are a funny agent. You respond with humor and wit.",
    "3": "You are a sad agent. You respond with sadness and melancholy."
}

message = []

class ChatRequest(BaseModel):
    message: str
    mode: str = "2"

@app.post("/chat")
def chat(request: ChatRequest):
    if not message:
        message.append(SystemMessage(content=modes.get(request.mode, modes["2"])))

    message.append(HumanMessage(content=request.message))

    try:
        response = model.invoke(message)
    except Exception as e:
        raise HTTPException(status_code=503, detail="The AI service is temporarily unavailable. Please try again in a moment.")

    message.append(AIMessage(content=response.content))
    return {"reply": response.content}