import os
from minio import Minio

bucket = "docbucket"
object_name = "shjdfhasjdfhaskjdfh2342lkjlk34_"
file_name = "Test.docx"

# Создаем клиент Minio
client = Minio(
    endpoint=os.getenv("ENDPOINT_URL"),
    access_key=os.getenv("ACCESS_KEY"),
    secret_key=os.getenv("SECRET_KEY"),
    secure=False,  # Если используется HTTPS, установите значение True
)


# Создаем новый баket, если его еще нет
try:
    client.make_bucket(bucket)
except Exception as err:
    if "BucketAlreadyOwnedByYou" not in str(err):
        raise

# Загрузка файла в Minio
try:
    client.fput_object(bucket, object_name, file_name)
except Exception as err:
    print(err)

# Получение объекта из Minio
try:
    client.fget_object(bucket, object_name, ".\download\Test2.docx")
except Exception as err:
    print(err)

# Удаление объекта из Minio
try:
    client.remove_object(bucket, object_name)
except Exception as err:
    print(err)
