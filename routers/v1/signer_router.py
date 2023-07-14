"""use these classes and modules in the code."""
from fastapi import APIRouter, Body
from aws.cloudfront import CloudFront

router = APIRouter()


async def startup_event():
    """
    The function "startup_event" prints a message indicating that the startup event has occurred.
    """
    print("Version 1: Startup event")


@router.post("/signedUrl")
async def generate_cloudfront_signed_url(s3_file_url: str = Body(..., embed=True)):
    """
    The function generates a signed URL for a file stored in Amazon S3 using CloudFront.
    """
    cloudfront = CloudFront()

    cloudfront_signed_url = cloudfront.get_signed_url(s3_file_url)

    return {"cloudfront_signed_url": cloudfront_signed_url}


async def shutdown_event():
    """
    The function `shutdown_event` prints a message indicating that a shutdown event has occurred.
    """
    print("Version 1: Shutdown event")


on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]
