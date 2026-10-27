from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import subprocess
import psutil
import time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="CHIP AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

class ChatRequest(BaseModel):
    message: str

class RunRequest(BaseModel):
    command: str

WHITELIST = ["git", "npm", "ls", "ps", "docker", "pm2", "systemctl"]

@app.post("/chat")
async def chat(req: ChatRequest):
    # Placeholder - integrate OpenAI/Anthropic
    return {"response": f"Agent received: {req.message}", "model": "placeholder"}

@app.post("/run")
async def run_command(req: RunRequest):
    cmd = req.command.split()[0]
    if cmd not in WHITELIST:
        raise HTTPException(400, "Command not allowed")
    try:
        result = subprocess.check_output(req.command, shell=True, stderr=subprocess.STDOUT, timeout=30)
        return {"output": result.decode()}
    except Exception as e:
        return {"error": str(e)}

@app.get("/status")
async def status():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime": time.time() - psutil.boot_time()
    }

@app.get("/logs")
async def logs():
    try:
        with open("logs.txt", "r") as f:
            return {"logs": f.readlines()[-100:]}
    except:
        return {"logs": ["No logs yet"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
