from fastapi import FastAPI, Depends
from app.auth.auth_bearer import JWTBearer
from app.controllers import auth, user, detection 

app = FastAPI()

# Status route
@app.get("/status")
async def ok():
    return {"status": "ok"}

# Protected route
@app.get("/protected", dependencies=[Depends(JWTBearer())])
async def protected_route():
    return {"message": "This is a protected route, if you see this you are authorized"}

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(detection.router)
