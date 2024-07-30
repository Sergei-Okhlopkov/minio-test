import os
from minio import Minio

minio_client = Minio(
    endpoint=os.getenv("ENDPOINT_URL"),
    access_key=os.getenv("ACCESS_KEY"),
    secret_key=os.getenv("SECRET_KEY"),
    secure=False,  # Если используется HTTPS, установите значение True
)
