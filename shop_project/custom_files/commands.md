# Установка проекта и подготовка окружения

# Клонировать репозиторий на локальную машину
git clone <URL_репозитория>

# Создать виртуальное окружение Python
python -m venv venv

# Разрешить выполнение скриптов в PowerShell (для активации окружения)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Активировать виртуальное окружение (Windows)
.\venv\Scripts\Activate

# Обновить pip до последней версии
python -m pip install --upgrade pip

# Установить зависимости из файла requirements.txt
pip install -r requirements.txt

# Подготовка базы данных и создание администратора

# Подготовить миграции для изменений в моделях
python manage.py makemigrations

# Применить миграции для создания/обновления таблиц в базе данных
python manage.py migrate

# Создать суперпользователя для панели администратора
python manage.py createsuperuser

# Запустить сервер разработки Django
python manage.py runserver

# Запустить телеграм бота
python manage.py startbot

# Работа с Git

# Добавить изменения в индекс (все файлы в текущей папке)
git add .

# Зафиксировать изменения с комментарием
git commit -m "Описание изменений"

# Отправить изменения в удалённый репозиторий (на основную ветку)
git push origin main

# Docker

# Остановка контейнеров:
docker-compose down

# Запуск контейнеров:
docker-compose up -d

# Сборка или пересборка контейнеров:
docker-compose build

# Сборка и запуск контейнеров
docker-compose up --build

# Просмотр логов:
docker-compose logs

# Или логи конкретного сервиса:
docker-compose logs web

# Открытие shell внутри контейнера:
docker exec -it <container_name> /bin/bash

# Просмотр запущенных контейнеров:
docker ps

# Команда для создания супеюзера:
docker exec -it shop_project-web-1 python manage.py shell

from django.contrib.auth import get_user_model
User = get_user_model()

user = User.objects.create_superuser('string', 'admin@example.com', 'string')
print("Superuser created successfully")

# Открытие SQL
psql -U electromanixbe kivano

# Сканирование проекта на наличие строк для перевода
python manage.py makemessages -l ru

# Компилирование переводов
python manage.py compilemessages
