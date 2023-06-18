from datetime import date
from pydantic import BaseModel, Field

class CreatePatientDto(BaseModel):
    first_name: str
    last_name: str
    gender: str = Field(default=None, max_length=2)
    country: str
    email: str
    birthday: date
