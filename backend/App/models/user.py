# schema
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    password: str
    email: str
    fullname: str

