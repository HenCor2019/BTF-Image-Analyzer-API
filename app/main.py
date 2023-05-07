import uvicorn
from fastapi import FastAPI, UploadFile, Body, Depends, File
import requests
import json
from app.constants.tensorflow_url import TENSORFLOW_MODEL_BASE_URL
from app.utils.image_processing import read_image_from_file

from app.model import UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

users = []

app = FastAPI()

# Status route
@app.get("/status")
async def read_ok():
    return {"status": "ok"}

# Protected route
@app.get("/protected", dependencies=[Depends(JWTBearer())])
async def protected_route():
    return {"message": "This is a protected route, if you see this you are authorized"}

# Auth Routes
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(default=None)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

# Brain Tumor Detection Routes
@app.post("/api/v1/analyze")
async def analyze_image(file: UploadFile = File(default=None)):
    normalized_image = await read_image_from_file(file)

    instances = normalized_image.reshape((1,)+normalized_image.shape).tolist()
    request_json = json.dumps({
         "signature_name": "serving_default",
         "instances": instances
    })
    response = requests.post(TENSORFLOW_MODEL_BASE_URL, data=request_json)
    response.raise_for_status()
    response = response.json()

    predictions = response['predictions'][0]
    return {
        'tumor_detection': {
            'no_tumor':  predictions[0],
            'tumor': predictions[1]
        }
    }
