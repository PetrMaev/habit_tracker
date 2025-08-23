from django.core.management import call_command
from django.core.management.base import BaseCommand

from habits.models import Habit, PleasantHabit


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        Habit.objects.all().delete()
        PleasantHabit.objects.all().delete()

        call_command("loaddata", "habit_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))

        call_command("loaddata", "pleasant_habit_fixture.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
