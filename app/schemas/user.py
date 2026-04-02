from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

#Common fields shared by all schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str

#Creating a user (SignUp)
class UserCreate(UserBase):
    password: str

#Updating a user (Optional fields)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# API response
class UserDetail(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True # This tells Pydantic to be nice with SQLAlchemy

# For the list of users
class UserList(BaseModel):
    users: List[UserDetail]