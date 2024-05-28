from pydantic import BaseModel,Field
from datetime import datetime


def get_current_time():
    return datetime.now()

class Name(BaseModel):
    id: int
    name : str
    content : str
    created_at: datetime = Field(default_factory=get_current_time)