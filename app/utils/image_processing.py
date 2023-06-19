import cv2
from fastapi import UploadFile
import numpy as np

from app.utils.corp_image import crop_brain_contour


async def read_image_from_file(file: UploadFile):
    contents = await file.read()
    image_decoded = np.fromstring(contents,  np.uint8)
    img = cv2.imdecode(image_decoded, cv2.IMREAD_GRAYSCALE)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    image = cv2.resize(img_rgb, dsize=(240, 240), interpolation=cv2.INTER_CUBIC)
    corped_image = crop_brain_contour(image)
    normalized_image = corped_image / 255

    return normalized_image
