from fastapi import APIRouter, Depends
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate
from app.auth.deps import get_current_user

from app.models.user import User
from app.schemas.patient import CreatePatientDto, PatientOut
from app.services.patients import PatientService


router = APIRouter()

@router.post("/api/v1/patients", summary="Use it to create a new patient for a MRI", tags=["Patients"])
async def create_patient(create_patient_dto: CreatePatientDto, user: User = Depends(get_current_user)):
    db_patient = PatientService().create_patient(create_patient_dto)
    return db_patient

@router.get("/api/v1/patients/search", summary="Use it to search a top five based on first name", tags=["Patients"])
async def search_top_five(q: str, user: User = Depends(get_current_user)):
    db_patients = PatientService().search_top_five(q)
    return db_patients

@router.get("/api/v1/patients", summary="Use it search all patients", tags=["Patients"], response_model=LimitOffsetPage[PatientOut])
async def get_all(user: User = Depends(get_current_user)):
    db_patients = PatientService().find_all()
    return paginate(db_patients)
