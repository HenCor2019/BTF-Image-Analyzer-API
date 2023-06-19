from fastapi import  FastAPI
from fastapi_pagination import add_pagination
from app.controllers import auth, mailer, user, detection, patients, diagnostics
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
add_pagination(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Status route
@app.get("/status", tags=["Health check"])
async def ok():
    return {"status": "ok"}

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(detection.router)
app.include_router(mailer.router)
app.include_router(patients.router)
app.include_router(diagnostics.router)

add_pagination(app)
