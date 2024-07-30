from s3minio import minio_client

bucket = "docbucket"
object_name = "shjdfhasjdfhaskjdfh2342lkjlk34_"
file_name = "Test.docx"

# Создаем новый баket, если его еще нет
try:
    minio_client.make_bucket(bucket)
except Exception as err:
    if "BucketAlreadyOwnedByYou" not in str(err):
        raise

# Загрузка файла в Minio
try:
    minio_client.fput_object(bucket, object_name, file_name)
except Exception as err:
    print(err)

# Получение объекта из Minio
try:
    minio_client.fget_object(bucket, object_name, ".\download\Test2.docx")
except Exception as err:
    print(err)

# Удаление объекта из Minio
try:
    minio_client.remove_object(bucket, object_name)
except Exception as err:
    print(err)
