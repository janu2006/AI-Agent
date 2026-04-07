from pydantic import BaseModel
from typing import Optional, Dict

class Observation(BaseModel):
    ticket: str
    conversation_history: list
    status: str

class Action(BaseModel):
    action_type: str  # classify/respond/escalate/request_info
    content: Optional[str]

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Dict