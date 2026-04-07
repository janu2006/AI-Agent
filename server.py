from fastapi import FastAPI
from env.environment import SupportEnv
from env.models import Action

app = FastAPI()
env = SupportEnv()

@app.post("/reset")
async def reset():
    result = await env.reset("easy")
    return result.dict()

@app.post("/step")
async def step(action: dict):
    action_obj = Action(**action)
    result = await env.step(action_obj)
    return result.dict()

@app.get("/state")
async def state():
    return env.state()