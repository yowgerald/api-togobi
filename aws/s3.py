""" The `from` statements are importing various modules and classes """
import boto3

from config import app_settings


class S3:
    """The S3 class is a placeholder for future code."""

    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=app_settings.aws_access_key_id,
            aws_secret_access_key=app_settings.aws_secret_access_key,
            region_name=app_settings.aws_region,
        )

    def upload_fileobj(self, file, key, extra_args):
        """
        The `upload_fileobj` function uploads a file object to an AWS S3 bucket
        using the `upload_fileobj` method of the S3 client.
        """
        self.s3_client.upload_fileobj(
            file, app_settings.aws_s3_bucket, key, ExtraArgs=extra_args
        )
