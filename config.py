""" The `from` statements are importing various modules and classes """
from pydantic import BaseSettings


class Settings(BaseSettings):
    """The above class is a subclass of BaseSettings."""

    app_port: int = 8000

    aws_region: str = ""
    aws_s3_bucket: str = ""
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_cloudfront_url: str = ""
    aws_cloudfront_key_path: str = ""

    class Config:
        """
        The Config class has a variable called env_file
        that stores the name of the environment file.
        """

        env_file = ".env"


app_settings = Settings()
