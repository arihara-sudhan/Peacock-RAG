from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from langchain_setup import get_qa_chain
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

qa_chain = get_qa_chain()
class QuestionRequest(BaseModel):
    question: str
    chat_history: list

@app.post("/ask/")
async def ask_question(request: QuestionRequest):
    question = request.question
    chat_history = request.chat_history
    response = qa_chain({"question": question, "chat_history": chat_history})
    return {"answer": response['answer']}