# Секундомер

---
## Настройка проекта
Все команды вводятся в командную строку (терминал).

Клонирование проекта:
```commandline
git clone https://github.com/iMWC-IXIVI/timer-app.git
```
Создание виртуального окружения:
```commandline
python -m venv venv
```
Активация виртуального окружения:
```commandline
venv/Scripts/activate
```
Установка зависимостей:
```commandline
pip install -r req.txt
```
После этого необходимо создать exe файл, используя команду:
```commandline
pyinstaller --onefile --windowed --name=timer --icon=icon/timer.ico app/main.py
```
После команды будет создано 2 папки и 1 файл, папку build и файл main.spec можно удалить,
а внутри папки dist будет находиться наш скомпилированный файл timer.exe.

---
## Стек технологий

---

```
1. Tkinter (встроенная библиотека в Python)
2. PyInstaller (для создания exe файла)
```