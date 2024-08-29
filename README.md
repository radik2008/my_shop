# KAZAN STORE
Мой проект на боевом сервере: 
          https://diplomshop.pythonanywhere.com/
Интернет-магазин на Django, реализующий функциональность онлайн-продаж с использованием современных технологий.

## Функциональность
- Управление товарами и категориями
- Корзина покупок
- Оформление и управление заказами
- Регистрация и авторизация пользователей
- Административный интерфейс

## Технологии
- Backend: Django, Python
- Frontend: HTML, CSS, JavaScript, Bootstrap
- База данных: MySQL
- Кэширование: Redis
- Сервер: Nginx, Gunicorn

## Установка
1. Клонируйте репозиторий:  
   `git clone https://github.com/radik2008/my_shop.git`

2. Установите зависимости:  
   `pip install -r requirements.txt`

3. Выполните миграции:  
   `python manage.py migrate`

4. Создайте суперпользователя:  
   `python manage.py createsuperuser`

5. Запустите сервер:  
   `python manage.py runserver`

## Деплой
Для деплоя используйте сервер Nginx и WSGI (Gunicorn). Настройки находятся в файле `nginx.conf` и `gunicorn.service`.

## Лицензия
Этот проект лицензирован под MIT License.


          
