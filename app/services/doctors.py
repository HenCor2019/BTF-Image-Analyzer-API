from sqlalchemy import Column
from app.schemas import user as schemas
from app.models import user as models
from app.database import get_db

class DoctorService():
    def __init__(self):
        self.db = get_db()

    def create_doctor(self, doctor: schemas.UserCreate, user_id: Column[int]):
        db_user = models.Doctor(
            first_name=doctor.first_name,
            last_name=doctor.last_name,
            country=doctor.country,
            carne=doctor.carnet,
            user_id=user_id
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
