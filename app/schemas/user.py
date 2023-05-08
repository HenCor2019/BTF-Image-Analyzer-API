from pydantic import BaseModel

class UserBase(BaseModel):
    full_name: str
    email: str
    country: str
    medical_role: str

class UserCreate(UserBase):
    password: str

class UserPassword(BaseModel):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
