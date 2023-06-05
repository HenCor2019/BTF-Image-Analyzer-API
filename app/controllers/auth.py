from fastapi import APIRouter, Depends, HTTPException
from app.auth.auth_bearer_refresh import JWTRefreshBearer

from app.services.auth import AuthService
from app.schemas.user import UserLogin

router = APIRouter()

@router.post("/auth/login", tags=["Auth"])
def login_user(user: UserLogin):
    token = AuthService().login(user)
    if token == False:
        raise HTTPException(status_code=404, detail="User not found")
    return token

@router.post("/auth/{id}/refresh-token", dependencies=[Depends(JWTRefreshBearer())] ,tags=["Auth"])
def refresh_token(userId: str):
    tokens = AuthService().refresh_token(userId)
    if tokens == False:
        raise HTTPException(status_code=404, detail="User not found")
    return tokens

