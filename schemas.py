from pydantic import BaseModel, EmailStr
from typing import Optional, Dict

# User model for registration
class User(BaseModel):
    username: str
    email: str
    password: str

# User login model
class UserLogin(BaseModel):
    email: str
    password: str

# Model for linking ID
class LinkID(BaseModel):
    user_id: str
    linked_id: Optional[str] = None

# Model for user details
class UserDetails(BaseModel):
    user_id: str
    address: Optional[str] = None
    phone: Optional[str] = None
    preferences: Optional[Dict] = None