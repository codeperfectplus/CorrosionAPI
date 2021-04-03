"""
FastAPI-0.61.2

Main Script for GET and POST Request Route.
"""
import os
import cv2
import shutil
from PIL import Image
from os.path import join as joinpath
from fastapi import FastAPI, File, UploadFile, Form, status
from fastapi.responses import FileResponse
from fastapi.openapi.utils import get_openapi

import settings
from settings import UPLOADS_DIR, base_url
from utils import main_fun

app = FastAPI()

@app.get("/")
async def home():
    """ OpenCV FaceFilter RestAPI"""
    return (
        {
            "title": settings.title,
            "api_version": settings.api_version,
            "documentation": f"{settings.documentation_url}",
            "author": "Deepak Raj",
            "github": "https://github.com/codeperfectplus",
            "email": "deepak008@live.com",
            "supported_image_type": "{Jpg, Png}",
            "time": settings.current_time,
        }
    )


@app.get('/api/v1/boundingbox/')
async def boundingbox_faster_RCNN_GET():
    return (
        {
            "title": "Corrosion Detection Bounding Box",
            "API Version": settings.api_version,
            "status": "Create post request for face-detection",
            "documentation": f"{settings.documentation_url}",
        }
    )

@app.post('/api/v1/boundingbox/', status_code=status.HTTP_201_CREATED)
async def boundingbox_faster_RCNN_POST(image: UploadFile = File(None, media_type='image/jpeg')):
    if image.content_type == 'image/jpeg':
        filename = image.filename
        image_path = joinpath(UPLOADS_DIR, filename)
        with open(image_path, 'wb') as buffer:           
            shutil.copyfileobj(image.file, buffer)
        
        preprocess_img = main_fun(image_path)
        # change BGR image RGb
        #preprocess_img = cv2.cvtColor(preprocess_img, cv2.COLOR_BGR2RGB)
        output_image = Image.fromarray(preprocess_img, "RGB")
        output_image.save(image_path)

        return {
                    "title": settings.title,
                    "api_version": settings.api_version,
                    "file_name": filename,
                    "output_image_url": f"{base_url}/uploads/{filename}",
                    "image_retain_policy": "Image will not use in any purpose. It will be delete from server in some time. So Save your Output image.",
                    "time": settings.current_time,
                    "documentation": f"{settings.documentation_url}",
                }
    return {
        'status': 'Input File is not A Image'
    }

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title= settings.title,
        version= settings.api_version,
        description= "Corrosion-Detection API with Tensorflow and FastAPI",
        routes = app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
