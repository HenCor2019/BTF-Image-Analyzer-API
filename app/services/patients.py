from fastapi import HTTPException, status
from app import models
from app.database import get_db
from app.schemas.patient import CreatePatientDto
from app.utils.non_found import get_repeated_email_message

class PatientService():
    def __init__(self):
        self.db = get_db()

    def find_by_id(self, patient_id: str):
        return self.db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    def create_patient(self, patient: CreatePatientDto, lan: str, doctorId: int):
        repeated_patient = self.db.query(models.Patient).filter(models.Patient.email == patient.email).first()
        if repeated_patient is not None:
            message = get_repeated_email_message(lan)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            )
        db_patient = models.Patient(
            first_name=patient.first_name,
            last_name=patient.last_name,
            country=patient.country,
            email=patient.email,
            birthday=patient.birthday,
            gender=patient.gender,
            doctor_id=doctorId
        )
        self.db.add(db_patient)
        self.db.commit()
        self.db.refresh(db_patient)
        return db_patient

    def find_all(self, q: str, doctorId: str):
        return self.db.query(models.Patient).filter(models.Patient.doctor_id == doctorId).all()

    def search_top_five(self, q: str, doctorId: str):
        return self.db.query(models.Patient).filter(models.Patient.doctor_id == doctorId).filter(models.Patient.first_name.contains(q)).limit(5).all()
  
