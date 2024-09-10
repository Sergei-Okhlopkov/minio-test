import io
import os
from s3minio import minio_client
import clamd

bucket = os.getenv("MINIO_DOC_BUCKET")
object_name = "test_object_name.txt_uuid78ej_!njn4"
file_name = "test.txt"

try:
    cd = clamd.ClamdNetworkSocket()
    # test if server is reachable
    print()
    print(cd.ping())
    print()
except clamd.ConnectionError:
    raise ValueError(
        "could not connect to clamd server either by unix or network socket"
    )

with open(file_name, "rb") as f:
    file_content = f.read()  # Чтение содержимого файла

result = cd.instream(io.BytesIO(file_content))
print(result['stream'][0])
print()
print(result['stream'][1])

# if result is None:
#     print("File content is clean.")
# else:
#     print(f"Virus detected in file content: {result}")

# Создаем новый баket, если его еще нет
# if not minio_client.bucket_exists(bucket):
#     minio_client.make_bucket(bucket)

# # Загрузка файла в Minio
# try:
#     minio_client.fput_object(bucket, object_name, file_name)
# except Exception as err:
#     print(err)

# # Получение объекта из Minio
# try:
#     minio_client.fget_object(bucket, object_name, "./download/загружено.txt")
# except Exception as err:
#     print(err)

# Удаление объекта из Minio
# try:
#     minio_client.remove_object(bucket, object_name)
# except Exception as err:
#     print(err)
