# Greenatom

Тестовое задание для компании [Greenatom](https://www.greenatom.ru/).

## Описание проекта

Этот проект представляет собой чат, основанный на Django приложение с административной панелью и сбором статики, развернутое в Docker. Ниже приведены инструкции для запуска проекта, выполнения миграций, сбора статики и создания суперпользователя.

## Стэк
- Docker
- Docker Compose
- HTML
- Django
- JavaScript
- Bootstrap
- Nginx
- Gunicorn

## Установка и запуск проекта

**_В общей директории файл .env.example переименовать в .env и заполнить своими данными:_**
```
POSTGRES_DB='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
DB_NAME='postgres'
DB_HOST=db
DB_PORT=5432
DEBUG=False
SECRET_KEY= # django secret key
ALLOWED_HOSTS='localhost,127.0.0.1'
DATABASES=postgresql
``` 


**Клонировать репозиторий:**
```
https://github.com/Resurection1/Greenatom.git
```


**Создать и запустить контейнеры Docker, выполнить команду на сервере (версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):**
```
sudo docker compose up -d
```

**_Выполнить миграции:_**

```
docker exec greenatom-backend-1 python manage.py migrate 
```
Создание статики
```
docker exec greenatom-backend-1 python manage.py collectstatic
```
Создать супер пользователя
```
winpty docker exec -it greenatom-backend-1 python manage.py createsuperuser
```
Заполнить тестовыми данными 
```
docker exec greenatom-backend-1 python manage.py populate_db
```

## Примеры запросов
Регистрация
```
http://127.0.0.1:8000/auth/registration/
```
Авторизация
```
http://127.0.0.1:8000/auth/login/
```
Админ панель
```
http://127.0.0.1:8000/admin/
```
Основное поле после авторизщации
```
http://127.0.0.1:8000/
```


### Автор
[Podzorov Mihail] - https://github.com/Resurection1