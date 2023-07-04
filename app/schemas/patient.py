from datetime import date
from typing import Literal
from pydantic import BaseModel, validator

class CreatePatientDto(BaseModel):
    first_name: str
    last_name: str
    gender: Literal["F", "M"]
    country: str
    email: str
    birthday: date

    @validator("birthday")
    def validate_dob(cls, v, values, **kwargs):
        if v > date.today():
            raise ValueError("The date must be lower than today")
        return v

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
