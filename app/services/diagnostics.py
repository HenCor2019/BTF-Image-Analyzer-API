from fastapi import HTTPException, status
from app import models
from app.database import get_db
from app.schemas.diagnostics import UpdateDiagnosticDto

class DiagnosticService():
    def __init__(self):
        self.db = get_db()

    def find_all(self, doctor_id: int, name: str):
        return self.db.query(models.Diagnostic).filter(models.Diagnostic.doctor_id == doctor_id).all()

    def evaluate(self, doctor_id: int, diagnostic_id: str, update_diagnostic_dto: UpdateDiagnosticDto):
        diagnostic = self.db.query(models.Diagnostic).filter(models.Diagnostic.id == diagnostic_id).first()
        if diagnostic is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The diagnostic could not be found in our system, please try again or try again later",
            )

        if diagnostic.doctor_id is not doctor_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The diagnosis cannot be evaluated, it belongs to a different doctor, please try again or try again later",
            )

        diagnostic.remark = update_diagnostic_dto.remark
        diagnostic.result_by_doctor = 1 if update_diagnostic_dto.is_approved is True else 0
        self.db.refresh(diagnostic)
