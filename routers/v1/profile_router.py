import boto3
from config import settings
import uuid
from datetime import datetime, timedelta
from fastapi import UploadFile, File, APIRouter
from aws.s3 import S3
from aws.cloudfront import CloudFront

router = APIRouter()

# Constants
PROFILE_IMAGES_PATH = "profiles/images/"

async def startup_event():
    print("Version 1: Startup event")


# Define the FastAPI endpoint to upload a file to S3
@router.post("/uploadImage")
async def upload_file(file: UploadFile = File(...)):
    s3_client = S3()
    cloudfront = CloudFront()

    extension = file.filename.split(".")[-1]
    filename = str(uuid.uuid4()) + "." + extension
    obj_key = PROFILE_IMAGES_PATH + filename

    extra_args = {
        "Metadata": {},
        "ContentType": file.content_type
    }

    s3_client.upload_fileobj(file.file, obj_key, extra_args)

    cloudfront_signed_url = cloudfront.get_signed_url(obj_key)

    return {
        "message": "File uploaded successfully",
        "signed_url": cloudfront_signed_url
    }

async def shutdown_event():
    print("Version 1: Shutdown event")

on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]