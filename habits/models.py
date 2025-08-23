from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PleasantHabit(models.Model):
    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Введите пользователя"
    )
    action = models.TextField(blank=True, null=True, verbose_name="Действие", help_text="Укажите действие")
    is_pleasant = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки", help_text="Привычка является приятной"
    )

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "приятная привычка"
        verbose_name_plural = "приятные привычки"


class Habit(models.Model):
    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, verbose_name="Пользователь", help_text="Введите пользователя"
    )
    place = models.TextField(
        blank=True, null=True, verbose_name="Место выполнения привычки", help_text="Укажите место выполнения привычки"
    )
    time = models.TimeField(
        blank=True, null=True, verbose_name="Время выполнения привычки", help_text="Укажите время выполнения привычки"
    )
    action = models.TextField(blank=True, null=True, verbose_name="Действие", help_text="Укажите действие")
    pleasant_habit = models.ForeignKey(
        PleasantHabit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Приятная привычка",
        help_text="Укажите приятную привычку",
    )
    periodicity = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message="Периодичность не может быть меньше 1 дня"),
            MaxValueValidator(7, message="Периодичность не может быть больше 7 дней"),
        ],
        default=1,
        verbose_name="Периодичность (дни)",
    )
    reward = models.TextField(
        blank=True, null=True, verbose_name="Вознаграждение", help_text="Укажите вознаграждение за выполнение привычки"
    )
    time_to_complete = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Время на выполнение привычки",
        help_text="Укажите время на выполнение привычки",
    )
    is_public = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name="Признак публичности привычки",
        help_text="Опубликовать привычку",
    )

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
