""" The code is importing necessary modules and classes for the code to work properly."""
import uuid
from fastapi import UploadFile, File, APIRouter
from aws.s3 import S3

router = APIRouter()

# Constants
PROFILE_IMAGES_PATH = "profiles/images/"


async def startup_event():
    """
    The function "startup_event" prints a message indicating that the startup event has occurred.
    """
    print("Version 1: Startup event")


@router.post("/uploadFile")
async def upload_file(file: UploadFile = File(...)):
    """
    The `upload_profile_image` function uploads a file to an S3 bucket and returns a success message
    along with the S3 URL of the uploaded file.
    """
    s3_client = S3()

    extension = file.filename.split(".")[-1]
    filename = str(uuid.uuid4()) + "." + extension
    obj_key = PROFILE_IMAGES_PATH + filename

    extra_args = {"Metadata": {}, "ContentType": file.content_type}

    s3_client.upload_fileobj(file.file, obj_key, extra_args)

    return {"message": "File uploaded successfully", "s3_url": obj_key}


async def shutdown_event():
    """
    The function `shutdown_event` prints a message indicating that a shutdown event has occurred.
    """
    print("Version 1: Shutdown event")


on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]
