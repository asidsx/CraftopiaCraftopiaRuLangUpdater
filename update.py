import os
import shutil
import wget
from zipfile import ZipFile
import sys
import time

url = "https://github.com/asidsx/AdditionalLanguagesForCraftopia/archive/refs/heads/20230711.2120.zip"

zip_file_name = "20230711.2120.zip"
extracted_folder_name = "AdditionalLanguagesForCraftopia-20230711.2120"

print("Скачивание архива:")
wget.download(url, out=zip_file_name)

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
