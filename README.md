# CraftopiaCraftopiaRuLangUpdater
---
Что бы использовать его, скачайте файл [update.exe](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/releases) и положите его сюда
\steamapps\workshop\content\1307550\2704964982\plugins\lang в папку мода где лежат файлы перевода.
И запустите его, он сам скачает актуальную версию и установит её, что бы можно было удобно им пользоваться создайте для него ярлык в любое удобное для вас место.

## Или можете сами скомпилировать программу.
Установите Python с галочной на PATH
Дальше установите зависимость requests
Запустив соммандрную строку CMD и выполните там это 
```
pip install requests pyinstaller
```
Дальше скачайте файл update.py и положите в пустую папку, дальше введите в адресной строке проводника где находится update.py 
![image](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/assets/106923482/06d13d12-85eb-4147-b1bc-3cf1d0ead3e7)
```
CMD
```



Дальше запустится коммандная строка и введите там это pyinstaller update.py --onefile   что бы скомпилировать файл update.exe
Дальше сделайте как в инструкции вверху
