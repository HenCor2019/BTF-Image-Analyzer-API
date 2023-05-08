from app.schemas import user as schemas
from app.models import user as models
from app.database import get_db
from app.utils.hash import verify_password
from app.auth.auth_handler import signJWT

class AuthService():
    def __init__(self):
        self.db = get_db()

    def login(self, user: schemas.UserLogin):
        db_user = self.db.query(models.User).filter(models.User.email == user.email).first()
        print(db_user.password)
        print(user.password)
        if db_user is None:
            return False

        if verify_password(user.password, db_user.password) == False:
            return False
        
        return signJWT(db_user.id)