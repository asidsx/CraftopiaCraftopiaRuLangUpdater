import os
import shutil
import wget
from zipfile import ZipFile
import sys
import time
import winreg

url = "https://github.com/asidsx/AdditionalLanguagesForCraftopia/archive/refs/heads/20230711.2120.zip"
zip_file_name = "20230711.2120.zip"
extracted_folder_name = "AdditionalLanguagesForCraftopia-20230711.2120"

print("Скачивание архива:")
wget.download(url, out=zip_file_name)

print("\nИзвлечение архива...")
with ZipFile(zip_file_name, "r") as zip_ref:
    zip_ref.extractall()

# Чтение пути из реестра
key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 1307550"
value_name = "InstallLocation"

try:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    install_location = winreg.QueryValueEx(key, value_name)[0]
    winreg.CloseKey(key)

    # Удаление части пути
    install_location = os.path.normpath(install_location)
    install_location = os.path.join(*install_location.split(os.sep)[:-2])

    # Модификация пути
    modified_path = os.path.join(install_location, "workshop", "content", "1307550", "2704964982", "plugins", "lang")
    modified_path = os.path.normpath(modified_path)  # Используем для обеспечения кросс-платформенности

    src_path = os.path.join(extracted_folder_name, "plugins", "lang", "ru.json")
    dst_path = os.path.join(modified_path, "ru.json")

    # Копирование файла
    shutil.copy(src_path, dst_path)

    print("Замена произведена. Очистка временных файлов...")
    os.remove(zip_file_name)
    shutil.rmtree(extracted_folder_name)

    print("Готово! Закрытие через 2 секунды...")
    time.sleep(2)
    sys.exit()

except Exception as e:
    print(f"Ошибка при чтении реестра: {e}")
    sys.exit(1)
