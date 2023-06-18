from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    first_name: str
    last_name: str
    carnet: str
    country: str
    password: str

class UserPassword(BaseModel):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TokenPayload(BaseModel):
    user_id: str = None
    expires: int = None

class UserOut(BaseModel):
    id: int
    email: str

class SystemUser(UserOut):
    password: str

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
