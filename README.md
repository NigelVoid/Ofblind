# Проект Ofblind (Django)

Инструкция по развертыванию и локальному запуску проекта на операционной системе Ubuntu / WSL.

## Требования
* Python 3.14+
* APT (Ubuntu/Debian)

---

## Первый запуск проекта

### 1. Подготовка системы (только для Linux/WSL)
```bash
sudo apt update
sudo apt install python3.14-venv
```

### 2. Настройка виртуального окружения
```bash
# Создание окружения
python3 -m venv .venv

# Активация окружения
source .venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Настройка базы данных
```bash
python manage.py migrate
```

### 5. Создание аккаунта администратора (Опционально)
```bash
python manage.py createsuperuser
```
### 6. Создание файла окружения .env (в папке проекта Django рядом с manage.py)
>[!WARNING]
>Обязательно меняйте данные на свои!

>[!NOTE]
>SECRET_KEY — секретный ключ шифрования  
>EMAIL_USER — gmail почта с которой будут рассылаться письма  
>EMAIL_PASSWORD — не пароль от аккаунта, а 16-значный код в Google App Passwords  
>DEBUG — при разработке обязательно значение True  
```
SECRET_KEY=yoursecretkey
EMAIL_USER=yourmail@gmail.com
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx
DEBUG=True
```
---

## Ежедневный запуск проекта

>[!WARNING]
>Команда запускается из папки проекта, в которой лежит .venv
```bash
# 1. Активировать окружение
source .venv/bin/activate
```
>[!WARNING]
>Команда запускается из папки проекта Django!(где лежит manage.py)
```bash
# 2. Запустить сервер разработки
python manage.py runserver
```

---

## Обновление библиотек(Для разработчиков):

```bash
# Обновление списка необходимых библиотек
pip freeze > requirements.txt
```

## Структура проекта
* `ofblind/` — папка с главными конфигурационными файлами проекта.
* `main/` — основное приложение сайта (логика, представления, шаблоны).
* `users/` — приложения с пользователями(авторизация, профили)
* `manage.py` — утилита командной строки Django для управления проектом.

---
# Полезные фишки-шаблоны

## Удаление пользователя из базы данных

```bash
python manage.py shell
```
> [!NOTE]
> Вписать в username= желаемого пользователя
```bash
from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='').delete()
```
```bash
exit()
```
