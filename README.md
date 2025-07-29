# Проект веб-приложения трекера полезных привычек
## Описание:
**Данное приложение предполагает создание SPA веб-приложения трекера полезных привычек.**
## Цель проекта:
Реализовать приложение, которое позволяет пользователям добавлять свои полезные привычки с возможностью напоминания о них.
## Установка:
1. Клонируйте репозиторий:
```python
https://github.com/PetrMaev/habit_tracker.git
```
```python
git@github.com:PetrMaev/habit_tracker.git
```
2. Установите зависимости:
```python
poetry install
```
## Наполнение данными базы данных:
Для наполнения данными базы данных используйте фикстуры и кастомные команды.
1. Кастомная команда для заполнения базы данных:
```python
python manage.py add_data
```
2. Кастомная команда для создания суперпользователя:
```python
python manage.py csu
```
3. Кастомная команда для создания группы модераторов и добавления пользователя-модератора:
```python
python manage.py create_moderator
```
## Использование:
Для запуска программы введите в терминале следующую команду:
```python
python manage.py runserver
```
## В проекте реализованы:
1. CRUD операции с привычками на базе Generics
2. Регистрация
3. Авторизация
4. Валидация на выбор связанной привычки и указания вознаграждения 
5. Пагинация списка привычек
6. Интеграция сервиса с мессенджером Telegram, который занимается рассылкой уведомлений
## Документация:
- Документация [Django](https://django.fun/docs/django/5.2/)
- Документация [Django Rest Framework](https://www.django-rest-framework.org/)
- Документация [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
- Документация [Celery](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)