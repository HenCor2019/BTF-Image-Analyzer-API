from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.deps import get_current_user, get_refresh_user
from app.models.user import Doctor, User

from app.services.auth import AuthService
from app.schemas.user import TokenSchema
from app.utils.non_found import get_non_found_user_message

router = APIRouter()

@router.post("/api/v1/auth/login", tags=["Auth"], response_model=TokenSchema)
def login_user(user_data: OAuth2PasswordRequestForm = Depends(), lan: str = "en"):
    token = AuthService().login(user_data)
    if token is False:
        message = get_non_found_user_message(lan)
        raise HTTPException(status_code=404, detail=message)
    return token

@router.post("/api/v1/auth/refresh-token", summary="Use it to refresh access token" ,tags=["Auth"])
def refresh_token(user: User = Depends(get_refresh_user), lan: str = "en"):
    tokens = AuthService().refresh_token(user.id)
    if tokens is False:
        message = get_non_found_user_message(lan)
        raise HTTPException(status_code=404, detail=message)
    return tokens

@router.get('/api/v1/auth/me', summary='Get details of currently logged in user', tags=["Auth"])
async def get_me(user: User = Depends(get_current_user)):
    doctor: Doctor = user.doctors[0]
    return {
        'doctor_id': doctor.id,
        'email': user.email,
        'first_name': doctor.first_name,
        'last_name': doctor.last_name,
        'carnet': doctor.carne,
        'country': doctor.country,
    }
