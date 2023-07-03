from pydantic import BaseSettings

class Settings(BaseSettings):
    app_port: int = 8000

    aws_region: str = ""
    aws_s3_bucket: str = ""
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_cloudfront_url: str = ""
    aws_cloudfront_key_path: str = ""

    class Config:
        env_file = ".env"

settings = Settings()