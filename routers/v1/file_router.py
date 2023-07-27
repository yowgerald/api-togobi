""" The code is importing necessary modules and classes for the code to work properly."""
from fastapi import UploadFile, File, APIRouter

from aws.s3 import S3

router = APIRouter()


async def startup_event():
    """
    The function "startup_event" prints a message indicating that the startup event has occurred.
    """
    print("Version 1: Startup event")


@router.post("/uploadFile")
async def upload_file(file: UploadFile = File(...)):
    """
    The `upload_file` function uploads a file to an S3 bucket and returns a success message.
    """
    s3_client = S3()

    extra_args = {"Metadata": {}, "ContentType": file.content_type}
    s3_client.upload_fileobj(file.file, file.filename, extra_args)

    return {"message": "File uploaded successfully"}


async def shutdown_event():
    """
    The function `shutdown_event` prints a message indicating that a shutdown event has occurred.
    """
    print("Version 1: Shutdown event")


on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]
