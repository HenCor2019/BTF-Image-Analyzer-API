from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from python_http_client import ForbiddenError
from sqlalchemy.schema import Column
from app.models import user as models
from app.database import get_db
from app.utils.hash import verify_password
from app.auth.auth_handler import signJWT

class AuthService():
    def __init__(self):
        self.db = get_db()

    def login(self, user: OAuth2PasswordRequestForm):
        db_user = self.db.query(models.User).filter(models.User.email == user.username).first()
        if db_user is None:
            return False

        if verify_password(user.password, db_user.password) is False:
            return False

        return signJWT(str(db_user.id))

    def refresh_token(self, id: Column[int]):
        db_user = self.db.query(models.User).filter(models.User.id == id).first()
        if db_user is None:
            return False

        return signJWT(str(db_user.id))
