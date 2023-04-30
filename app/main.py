from fastapi import FastAPI, UploadFile, File
import requests
import json
import numpy as np
import cv2

app = FastAPI()


BASE_URL = "http://localhost:8501/v1/models/brain_tumor_detection:predict"


async def read_image(file: UploadFile):
    contents = await file.read()
    image_decoded = np.fromstring(contents,  np.uint8)
    img = cv2.imdecode(image_decoded, cv2.IMREAD_UNCHANGED)
    image = cv2.resize(img, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
    normalized_image = image / 255

    return normalized_image


@app.get("/healthcheck")
async def read_ok():
    return "ok"


@app.post("/api/v1/analyze")
async def analyze_image(file: UploadFile = File(...)):
    normalized_image = await read_image(file)

    instances = normalized_image.reshape((1,)+normalized_image.shape).tolist()
    request_json = json.dumps({
         "signature_name": "serving_default",
         "instances": instances
    })
    response = requests.post(BASE_URL, data=request_json)
    response.raise_for_status()
    response = response.json()

    predictions = response['predictions'][0]
    return {
        'tumor_detection': {
            'no_tumor':  predictions[0],
            'tumor': predictions[1]
        }
    }
