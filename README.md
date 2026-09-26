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

---

## Ежедневный запуск проекта


```bash
# 1. Активировать окружение
source .venv/bin/activate

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
* `manage.py` — утилита командной строки Django для управления проектом.
