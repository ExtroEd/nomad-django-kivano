Установка проекта и подготовка окружения

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

Подготовка базы данных и создание администратора

# Подготовить миграции для изменений в моделях
python manage.py makemigrations

# Применить миграции для создания/обновления таблиц в базе данных
python manage.py migrate

# Создать суперпользователя для панели администратора
python manage.py createsuperuser

# Запустить сервер разработки Django
python manage.py runserver

Работа с Git

# Добавить изменения в индекс (все файлы в текущей папке)
git add .

# Зафиксировать изменения с комментарием
git commit -m "Описание изменений"

# Отправить изменения в удалённый репозиторий (на основную ветку)
git push origin main

# Добавить новый удалённый репозиторий (если ещё не добавлен)
git remote add origin <URL_репозитория>

# Изменить URL существующего удалённого репозитория
git remote set-url origin <URL_репозитория>

# Проверить URL текущего удалённого репозитория
git remote -v

# Принудительно отправить изменения в удалённый репозиторий (перезаписать)
git push origin main --force

# Получить последние изменения из удалённого репозитория
git pull origin main