from fastapi import APIRouter, Body
from aws.cloudfront import CloudFront
from typing import Annotated

router = APIRouter()

async def startup_event():
    print("Version 1: Startup event")


# Define the FastAPI endpoint to upload a file to S3
@router.post("/signedUrl")
async def generate_cloudfront_signed_url(s3_file_url: str = Body(..., embed=True)):
    cloudfront = CloudFront()
    
    cloudfront_signed_url = cloudfront.get_signed_url(s3_file_url)
    
    return {
        "cloudfront_signed_url": cloudfront_signed_url
    }


async def shutdown_event():
    print("Version 1: Shutdown event")

on_startup = [startup_event]
on_shutdown = [shutdown_event]

routes = [router]