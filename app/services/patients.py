from app import models
from app.database import get_db
from app.schemas.patient import CreatePatientDto

class PatientService():
    def __init__(self):
        self.db = get_db()

    def create_patient(self, patient: CreatePatientDto):
        db_patient = models.Patient(
            first_name=patient.first_name,
            last_name=patient.last_name,
            country=patient.country,
            email=patient.email,
            birthday=patient.birthday,
            gender=patient.gender
        )
        self.db.add(db_patient)
        self.db.commit()
        self.db.refresh(db_patient)
        return db_patient

    def search_top_five(self, q: str):
        return self.db.query(models.Patient).filter(models.Patient.first_name.contains(q)).limit(5).all()
