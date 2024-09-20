import asyncio
import io
import os
from s3minio import minio_client
import aioclamd


async def main():
    bucket = os.getenv("MINIO_DOC_BUCKET")
    object_name = "test_object_name.txt_uuid78ej_!njn4"
    file_name = "test.txt"

    try:
        cd = aioclamd.ClamdAsyncClient()
        # test if server is reachable
        print()
        print(await cd.ping())
        print()
    except aioclamd.ClamdConnectionError:
        raise ValueError(
            "could not connect to clamd server either by unix or network socket"
        )

    with open(file_name, "rb") as f:
        file_content = f.read()  # Чтение содержимого файла

    result = await cd.instream(io.BytesIO(file_content))
    print(result['stream'][0])
    print()
    print(result['stream'][1])

    if result is None:
        print("File content is clean.")
    else:
        print(f"Virus detected in file content: {result}")

    # # Создаем новый баket, если его еще нет
    # if not minio_client.bucket_exists(bucket):
    #     minio_client.make_bucket(bucket)

    # # Загрузка файла в Minio
    # try:
    #     await minio_client.fput_object(bucket, object_name, file_name)
    # except Exception as err:
    #     print(err)

    # # Получение объекта из Minio
    # try:
    #     await minio_client.fget_object(bucket, object_name, "./download/загружено.txt")
    # except Exception as err:
    #     print(err)

    # # Удаление объекта из Minio
    # try:
    #     minio_client.remove_object(bucket, object_name)
    # except Exception as err:
    #     print(err)

if __name__ == "__main__":
    asyncio.run(main())
