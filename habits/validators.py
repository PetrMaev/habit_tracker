from rest_framework import serializers

from habits.models import PleasantHabit


class RewardValidator:
    __fields__ = ["pleasant_habit", "reward"]

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        pleasant_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if pleasant_habit and reward:
            raise serializers.ValidationError("Нельзя одновременно выбрать приятную привычку и вознаграждение.")


class TimeToCompleteValidator:
    __fields__ = ["time_to_complete"]

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = dict(value).get(self.field)
        if time_to_complete is not None:
            if int(time_to_complete) > 120:
                raise serializers.ValidationError("Время на выполнение привычки не может быть больше 120 секунд")
        else:
            return value


class PleasantHabitValidator:
    __fields__ = ["pleasant_habit"]

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pleasant_habit_value = dict(value).get(self.field)

        if pleasant_habit_value:
            try:
                if hasattr(pleasant_habit_value, "is_pleasant"):
                    pleasant_habit = pleasant_habit_value
                else:
                    pleasant_habit_id = int(pleasant_habit_value)
                    pleasant_habit = PleasantHabit.objects.get(id=pleasant_habit_id)

                if not pleasant_habit.is_pleasant:
                    raise serializers.ValidationError(
                        "В связанные привычки могут попадать только привычки с признаком приятной привычки"
                    )

            except (ValueError, TypeError):
                raise serializers.ValidationError("Некорректный формат привычки")
            except Exception:
                raise serializers.ValidationError("Связанная привычка не найдена")

        return value
