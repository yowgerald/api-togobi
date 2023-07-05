import uuid
from fastapi import UploadFile, File, APIRouter
from aws.s3 import S3

router = APIRouter()

# Constants
PROFILE_IMAGES_PATH = "profiles/images/"

async def startup_event():
    print("Version 1: Startup event")


@router.post("/uploadImage")
async def upload_file(file: UploadFile = File(...)):
    s3_client = S3()

    extension = file.filename.split(".")[-1]
    filename = str(uuid.uuid4()) + "." + extension
    obj_key = PROFILE_IMAGES_PATH + filename

    extra_args = {
        "Metadata": {},
        "ContentType": file.content_type
    }

    s3_client.upload_fileobj(file.file, obj_key, extra_args)

    return {
        "message": "File uploaded successfully",
        "s3_url": obj_key
    }


async def shutdown_event():
    print("Version 1: Shutdown event")


on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]