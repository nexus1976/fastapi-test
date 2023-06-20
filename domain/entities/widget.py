import uuid
from pydantic import BaseModel

class Widget(BaseModel):
    id: uuid.UUID = uuid.UUID(int=0)
    name: str = ''
    