from app.schemas import user as schemas
from app.models import user as models
from app.database import get_db
from app.utils.hash import get_password_hash

class UserService():
    def __init__(self):
        self.db = get_db()

    def create_user(self, user: schemas.UserCreate):
        db_user = models.User(
            email=user.email, 
            full_name=user.full_name, 
            password=get_password_hash(user.password),
            country=user.country,
            medical_role=user.medical_role
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
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
        if user.full_name is not None:
            db_user.full_name = user.full_name
        if user.password is not None:
            db_user.password = get_password_hash(user.password)
        if user.country is not None:
            db_user.country = user.country
        if user.medical_role is not None:
            db_user.medical_role = user.medical_role
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
