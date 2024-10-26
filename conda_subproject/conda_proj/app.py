"""Backend interface for interacting with the agent lifecycle.

Example command to run: uvicorn api_server:app --host 0.0.0.0 --port 1337
"""

from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
app = FastAPI()

hello_world_router = APIRouter()

class HelloWorldResponse(BaseModel):
    response: str

@hello_world_router.get("/hello-world")
async def hello_world():
    return HelloWorldResponse(response="Hello world!")
    
    