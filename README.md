# CraftopiaCraftopiaRuLangUpdater
![GitHub all releases](https://img.shields.io/github/downloads/asidsx/CraftopiaCraftopiaRuLangUpdater/total)

---
Что бы использовать его, скачайте файл [update.exe](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/releases) и положите его сюда
"\steamapps\workshop\content\1307550\2704964982\plugins\lang" в папку мода где лежат файлы перевода.  
И запустите его, он сам скачает актуальную версию и установит её, что бы можно было удобно им пользоваться создайте для него ярлык в любое удобное для вас место.  <details>
  <summary>а как сделать ярлык?</summary>
  Чтобы создать ярлык на исполняемый файл в Windows, выполните следующие действия:

1. Найдите исполняемый файл, для которого вы хотите создать ярлык.
2. Нажмите правой кнопкой мыши на исполняемый файл и выберите "Отправить на рабочий стол (ярлык)" После можно его копировать в любое место с рабочего стола.
</details>  

<b>Обновление</b>  
Я тут добавил новый [релиз](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/releases/tag/Rs-reg), который должен считывать ветки реестра к моду, и заменять файл уже там(программу больше не нужно копировать в папке "lang"), но я не знаю как это будет работать у всех, так что тестите.

## Или можете сами скомпилировать программу.
Установите Python с галочкой на PATH  
Дальше установите зависимость requests  
Запустив командную строку CMD и выполните там это  

```
pip install wget pyinstaller
```
Дальше скачайте файл update.py и положите в пустую папку, дальше введите в адресной строке проводника, где находится update.py  
![image](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/assets/106923482/06d13d12-85eb-4147-b1bc-3cf1d0ead3e7)
```
CMD
```



Дальше запустится командная строка и введите там это 
```
pyinstaller update.py --onefile
```
или
```
pyinstaller updatereg.py --onefile
```
что бы скомпилировать файл update.exe, он будет в папке dist  
![image](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/assets/106923482/cd750da7-a83b-4abb-9f47-ada48fedf7f5)

Дальше сделайте как в инструкции вверху


Программа скачивает актаульный перевод отсюда https://github.com/asidsx/AdditionalLanguagesForCraftopia

## Важно!
Если у вас происходит при запуске игры отписка от модов
то скопируйте эти 2 файла в архиве в папку с игрой и отписка прекратится.
[formod.rar](https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/blob/main/formod.rar)https://github.com/asidsx/CraftopiaCraftopiaRuLangUpdater/blob/main/formod.rar
