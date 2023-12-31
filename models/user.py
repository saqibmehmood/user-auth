from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = None
