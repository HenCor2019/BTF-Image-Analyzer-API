from fastapi import APIRouter, Depends
from python_http_client import ServiceUnavailableError
from starlette.responses import JSONResponse

from app.auth.auth_bearer import JWTBearer
from app.libs.mailer import send_mail


router = APIRouter()

@router.post("/contact", dependencies=[Depends((JWTBearer()))])
async def contact_with_us():
    try:
        await send_mail('henry200amaya@gmail.com')
        return JSONResponse(status_code=200, content={'success': True})
    except:
        return JSONResponse(status_code=400, content={'success': False})
