# DevOps_creator v0.4
Cоздаёт структуру папок для нового проекта + текстовые файлы



Как пользоваться:
Cкачай себе DevOps_creator v0.4.exe
Запусти его в папке где у тебя будут все проекты. Если не писать путь создания проекта - проект создастся в папке где лежит.



Если хочешь добавить функционал и оттестить:

Зависимости:
Надо будет либа PySimpleGUI

Команда билда приложения. Билд происходил из win11
pyinstaller -F -w -i "C:\DevOps_create_new_project\icon.ico" DevOps_creator.py

Поудобнее билдить с граф оберткой https://habr.com/ru/company/vdsina/blog/557316/
auto-py-to-exe

#pip install pypiwin32