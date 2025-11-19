from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from datetime import datetime

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate

app = FastAPI(
    title="AI Chatbot with LangChain",
    description="FastAPI backend with LangChain integration for AI-powered conversations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    response: str
    session_id: str
    timestamp: str

class ConversationHistory(BaseModel):
    messages: List[dict]

# In-memory storage for conversation histories
conversation_store = {}

def get_llm():
    """Initialize and return LangChain LLM"""
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    return ChatOpenAI(
        temperature=0.7,
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key
    )

def get_conversation_chain(session_id: str):
    """Get or create conversation chain for session"""
    if session_id not in conversation_store:
        memory = ConversationBufferMemory(return_messages=True)
        llm = get_llm()
        conversation_store[session_id] = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True
        )
    return conversation_store[session_id]

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AI Chatbot API with LangChain",
        "version": "1.0.0",
        "endpoints": ["/chat", "/history/{session_id}", "/clear/{session_id}"]
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process chat message and return AI response"""
    try:
        chain = get_conversation_chain(request.session_id)
        response = chain.predict(input=request.message)
        
        return ChatResponse(
            response=response,
            session_id=request.session_id,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/{session_id}", response_model=ConversationHistory)
async def get_history(session_id: str):
    """Get conversation history for a session"""
    if session_id not in conversation_store:
        return ConversationHistory(messages=[])
    
    chain = conversation_store[session_id]
    messages = chain.memory.chat_memory.messages
    
    history = []
    for msg in messages:
        if isinstance(msg, HumanMessage):
            history.append({"role": "user", "content": msg.content})
        elif isinstance(msg, AIMessage):
            history.append({"role": "assistant", "content": msg.content})
    
    return ConversationHistory(messages=history)

@app.delete("/clear/{session_id}")
async def clear_history(session_id: str):
    """Clear conversation history for a session"""
    if session_id in conversation_store:
        del conversation_store[session_id]
        return {"message": f"History cleared for session {session_id}"}
    return {"message": f"No history found for session {session_id}"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
