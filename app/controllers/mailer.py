from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse
from app.auth.deps import get_current_user

from app.libs.mailer import send_mail
from app.models.user import User


router = APIRouter()
CONTACT_EMAIL = 'henry200amaya@gmail.com'

@router.post("/api/v1/contact", tags=["Contact us"])
async def contact_with_us(user: User = Depends(get_current_user)):
    try:
        await send_mail(CONTACT_EMAIL)
        return JSONResponse(status_code=200, content={'success': True})
    except:
        return JSONResponse(status_code=400, content={'success': False})
