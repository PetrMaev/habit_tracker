from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_tg_message() -> None:
    """Отправляет сообщение пользователю в телеграмм"""
    start_time = timezone.localtime()
    end_time = start_time + timedelta(minutes=1)
    habits = Habit.objects.filter(time__range=(start_time.time(), end_time.time()))
    for habit in habits:
        user = habit.user
        message = f"Пора {habit.action}"
        if user.tg_chat_id:
            send_telegram_message(message, user.tg_chat_id)
