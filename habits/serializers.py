from rest_framework import serializers

from habits.models import Habit, PleasantHabit
from habits.validators import PleasantHabitValidator, RewardValidator, TimeToCompleteValidator


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Habit
        fields = [
            "id",
            "user",
            "place",
            "time",
            "action",
            "periodicity",
            "pleasant_habit",
            "reward",
            "time_to_complete",
        ]
        validators = [
            RewardValidator("pleasant_habit", "reward"),
            TimeToCompleteValidator(field="time_to_complete"),
            PleasantHabitValidator(field="pleasant_habit"),
        ]


class PleasantHabitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PleasantHabit
        fields = "__all__"
