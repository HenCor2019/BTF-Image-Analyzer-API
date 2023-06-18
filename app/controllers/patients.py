from typing import Annotated
from fastapi import APIRouter, Depends, Query
from app.auth.deps import get_current_user

from app.models.user import User
from app.schemas.patient import CreatePatientDto
from app.services.patients import PatientService


router = APIRouter()

@router.post("/api/v1/patients", summary="Use it to create a new patient for a MRI", tags=["Patients"])
async def create_patient(create_patient_dto: CreatePatientDto, user: User = Depends(get_current_user)):
    db_patient = PatientService().create_patient(create_patient_dto)
    return db_patient

@router.get("/api/v1/patients/search", summary="Use it to search a top five based on email", tags=["Patients"])
async def create_patient(q: Annotated[str, Query(default=None,min_length=3, max_length=30)], user: User = Depends(get_current_user)):
    db_patients = PatientService().search_top_five(q)
    return db_patients
