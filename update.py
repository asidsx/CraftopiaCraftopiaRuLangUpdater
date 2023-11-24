import os
import shutil
import requests
from zipfile import ZipFile
import sys
import time


url = "https://github.com/asidsx/AdditionalLanguagesForCraftopia/archive/refs/heads/20230711.2120.zip"


zip_file_name = "20230711.2120.zip"
extracted_folder_name = "AdditionalLanguagesForCraftopia-20230711.2120"


print("Скачивание архива:")
response = requests.get(url, stream=True)
total_size_in_bytes = int(response.headers.get('content-length', 0))
block_size = 1024  
downloaded_size = 0

with open(zip_file_name, "wb") as zip_file:
    for data in response.iter_content(block_size):
        downloaded_size += len(data)
        progress = int(50 * downloaded_size / total_size_in_bytes)
        sys.stdout.write("\r[%-50s] %d%%" % ('#' * progress, 2 * progress))
        sys.stdout.flush()
        zip_file.write(data)

print("\nИзвлечение архива...")

with ZipFile(zip_file_name, "r") as zip_ref:
    zip_ref.extractall()


src_path = os.path.join(extracted_folder_name, "plugins", "lang", "ru.json")
dst_path = os.path.join(os.getcwd(), "ru.json")
shutil.copy(src_path, dst_path)


print("Замена произведена. Очистка временных файлов...")
os.remove(zip_file_name)
shutil.rmtree(extracted_folder_name)

print("Готово! Закрытие через 2 секунды...")
time.sleep(2)
sys.exit()
