from datetime import date
from pydantic import BaseModel

from app.schemas.patient import PatientOut

class DiagnosticOut(BaseModel):
    id: str
    image_url: str
    positive_probability: float
    negative_probability: float
    result_by_doctor: int
    created_at: date

    patient: PatientOut

    class Config:
        orm_mode = True
