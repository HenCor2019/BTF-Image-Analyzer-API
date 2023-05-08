from fastapi import APIRouter, HTTPException

from app.services.auth import AuthService
from app.schemas.user import UserLogin

router = APIRouter()

@router.post("/auth/login")
def login_user(user: UserLogin):
    token = AuthService().login(user)
    if token == False:
        raise HTTPException(status_code=404, detail="User not found")
    return token
