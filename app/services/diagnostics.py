from datetime import datetime
from fastapi import HTTPException, status
from app import models
from app.database import get_db
from app.schemas.diagnostics import UpdateDiagnosticDto
from app.utils.non_found import get_forbidden_diagnostic_message, get_non_found_diagnostic_message

class DiagnosticService():
    def __init__(self):
        self.db = get_db()

    def create_one(self, doctor_id: int, patient_id: str, src_url: str, positive_probability: float, negative_probability: float):
        saved_diagnostic = models.Diagnostic(
            image_url=src_url,
            positive_probability=positive_probability,
            negative_probability=negative_probability,
            result_by_doctor=0,
            remark="No reviewed yet",
            doctor_id=doctor_id,
            patient_id=patient_id,
            created_at=datetime.today()
        )
        self.db.add(saved_diagnostic)
        self.db.commit()
        self.db.refresh(saved_diagnostic)
        return saved_diagnostic

    def find_all(self, doctor_id: int, name: str):
        return self.db.query(models.Diagnostic).filter(models.Diagnostic.doctor_id == doctor_id).all()

    def evaluate(self, doctor_id: int, diagnostic_id: str, update_diagnostic_dto: UpdateDiagnosticDto, lan: str):
        diagnostic = self.db.query(models.Diagnostic).filter(models.Diagnostic.id == diagnostic_id).first()
        if diagnostic is None:
            message = get_non_found_diagnostic_message(lan)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            )

        if int(diagnostic.doctor_id) != int(doctor_id):
            message = get_forbidden_diagnostic_message(lan)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=message,
            )

        diagnostic.remark = update_diagnostic_dto.remark
        diagnostic.result_by_doctor = update_diagnostic_dto.is_approved
        self.db.commit()
        self.db.refresh(diagnostic)
