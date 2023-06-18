from datetime import date
from pydantic import BaseModel, Field

class CreatePatientDto(BaseModel):
    first_name: str
    last_name: str
    gender: str = Field(default=None, max_length=2)
    country: str
    email: str
    birthday: date

class PatientOut(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    email: str
    id: int
    gender: str
    country: str

    class Config:
        orm_mode = True
