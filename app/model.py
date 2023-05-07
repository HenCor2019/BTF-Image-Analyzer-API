from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "john@example.com",
                "password": "password"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "password"
            }
        }