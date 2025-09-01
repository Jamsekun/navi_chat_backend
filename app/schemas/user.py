from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    display_name: Optional[str] = None

class UserCreate(UserBase):
    firebase_uid: str

class UserUpdate(BaseModel):
    display_name: Optional[str] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
