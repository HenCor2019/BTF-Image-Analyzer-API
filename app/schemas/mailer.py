from pydantic import BaseModel


class CreateMailDto(BaseModel):
    email: str
    name: str
    subject: str
    content: str
