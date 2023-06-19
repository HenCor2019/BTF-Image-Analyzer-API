from uuid import uuid4
import cloudinary
import cloudinary.uploader
import cloudinary.api
from fastapi import UploadFile
config = cloudinary.config(secure=True)

def upload_image(file: UploadFile):
    result =  cloudinary.uploader.upload(file)
    src_url = result.build_url()

    return src_url
