import boto3
from config import settings

class S3:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )

    def upload_fileobj(self, file, key, extra_args):
        self.s3_client.upload_fileobj(
            file,
            settings.aws_s3_bucket,
            key,
            ExtraArgs=extra_args
        )
