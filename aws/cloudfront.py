from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner
from config import settings

class CloudFront:
    @staticmethod
    def rsa_signer(message):
        with open(settings.aws_cloudfront_key_path, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

    @staticmethod
    def get_signed_url(object_key):
        expire_date = datetime.now() + timedelta(hours=1)

        cloudfront_signer = CloudFrontSigner(settings.aws_access_key_id, CloudFront.rsa_signer)
        signed_url = cloudfront_signer.generate_presigned_url(
            settings.aws_cloudfront_url + object_key, date_less_than=expire_date)

        return signed_url
