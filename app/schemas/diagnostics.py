from datetime import date
from typing import Literal
from pydantic import BaseModel, Field

from app.schemas.patient import PatientOut

class DiagnosticOut(BaseModel):
    id: str
    image_url: str
    positive_probability: float
    negative_probability: float
    result_by_doctor: int
    created_at: date
    remark: str

    patient: PatientOut

    class Config:
        orm_mode = True

class UpdateDiagnosticDto(BaseModel):
    is_approved: Literal[0, 1]
    remark: str
