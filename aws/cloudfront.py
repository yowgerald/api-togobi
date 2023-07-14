""" The `from` statements are importing various modules and classes """
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner
from config import app_settings


class CloudFront:
    """The CloudFront class is used for managing and interacting with CloudFront distributions."""

    @staticmethod
    def rsa_signer(message):
        """
        The `rsa_signer` function signs a message using an RSA private key.
        """
        with open(app_settings.aws_cloudfront_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(), password=None, backend=default_backend()
            )
        return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

    @staticmethod
    def get_signed_url(object_key):
        """
        The `get_signed_url` function generates a signed URL
        for accessing an object in an AWS CloudFront distribution.
        """
        expire_date = datetime.now() + timedelta(hours=1)

        cloudfront_signer = CloudFrontSigner(
            app_settings.aws_access_key_id, CloudFront.rsa_signer
        )
        signed_url = cloudfront_signer.generate_presigned_url(
            app_settings.aws_cloudfront_url + object_key, date_less_than=expire_date
        )

        return signed_url
