from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str
    temperature: float = 0.7

@app.post("/generate")
async def generate_text(request: ChatRequest):
    # Simulate LLM call
    await asyncio.sleep(1) 
    return {
        "response": f"Echo: {request.prompt}",
        "temp_used": request.temperature
    }

# Run with: uvicorn code.main:app --reload
