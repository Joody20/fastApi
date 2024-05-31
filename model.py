from pydantic import BaseModel,Field
from datetime import datetime
import pytz


def get_current_time():
    seoul_tz = pytz.timezone('Asia/Seoul')
    return datetime.now(seoul_tz)


class Name(BaseModel):
    id: int
    name : str
    content : str
    created_at: datetime = Field(default_factory=get_current_time)