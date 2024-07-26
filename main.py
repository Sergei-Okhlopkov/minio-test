import asyncio
from contextlib import asynccontextmanager
import os
from aiobotocore.session import get_session
from pathlib import PurePath


class S3Client:
    def __init__(
        self, access_key: str, secret_key: str, endpoint_url: str, bucket_name: str
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secrect_key_id": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", self.config) as client:
            yield client

    async def upload_file(self, file_path: str):
        async with self.get_client() as client:
            with open(file_path, "rb") as file:
                object_name = PurePath(file_path).parts[-1]
                await client.put_object(
                    Bucket=self.bucket_name, Key=object_name, Body=file
                )


async def main():
    s3_client = S3Client(
        access_key=os.getenv("ACCESS_KEY"),
        secret_key=os.getenv("SECRET_KEY"),
        endpoint_url=os.getenv("ENDPOINT_URL"),
        bucket_name="docs",
    )

    await s3_client.upload_file("Test.docx")


if __name__ == "__main__":
    asyncio.run(main())
