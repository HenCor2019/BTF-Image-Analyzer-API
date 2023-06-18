from app import models
from app.database import get_db

class DiagnosticService():
    def __init__(self):
        self.db = get_db()

    def find_all(self, doctor_id: int, name: str):
        return self.db.query(models.Diagnostic).filter(models.Diagnostic.doctor_id == doctor_id).all()
