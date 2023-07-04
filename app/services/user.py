from fastapi import HTTPException, status
from app.schemas import user as schemas
from app.models import user as models
from app.database import get_db
from app.services.doctors import DoctorService
from app.utils.hash import get_password_hash
from app.utils.non_found import get_repeated_carnet_message, get_repeated_email_message

class UserService():
    def __init__(self):
        self.db = get_db()

    def create_user(self, user: schemas.UserCreate, lan: str):
        repeated_user = self.db.query(models.User).filter(models.User.email == user.email).first()
        if repeated_user  is not None:
            message = get_repeated_email_message(lan)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            )
        repeated_doctor = self.db.query(models.Doctor).filter(models.Doctor.carne == user.carnet).first()
        if repeated_doctor is not None:
            message = get_repeated_carnet_message(lan)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            )
        db_user = models.User(
            email=user.email,
            password=get_password_hash(user.password),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        DoctorService().create_doctor(user, db_user.id)
        return db_user

    def get_users(self, skip: int = 0, limit: int = 100):
        users = self.db.query(models.User).offset(skip).limit(limit).all()
        return users

    def get_user(self, user_id: int):
        db_user = self.db.query(models.User).filter(models.User.id == user_id).first()
        if db_user is None:
            return None
        return db_user

    def update_user(self, user_id: int, user: schemas.UserPassword):
        db_user = self.get_user(user_id)
        if db_user is None:
            return None
        if user.email is not None:
            db_user.email = user.email
        if user.password is not None:
            db_user.password = get_password_hash(user.password)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user(user_id)
        if db_user is None:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return True
