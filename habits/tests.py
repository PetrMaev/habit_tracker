from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, PleasantHabit
from users.models import CustomUser


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email="tester@sky.pro")
        self.pleasant_habit = PleasantHabit.objects.create(user=self.user, action="Ванна с пеной", is_pleasant=True)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Парк",
            time="07:00",
            action="Бегать",
            periodicity=1,
            pleasant_habit=self.pleasant_habit,
            time_to_complete=120,
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тестирование просмотра привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        """Тестирование создания привычки."""
        url = reverse("habits:habit-create")
        data = {
            "place": "На встречу",
            "action": "Не опаздывать",
            "periodicity": 1,
            "reward": "Десерт",
            "is_public": False,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тестирование изменения привычки."""

        url = reverse("habits:habit-edit", args=(self.habit.pk,))
        data = {"place": "Набережная"}
        response = self.client.patch(url, data)

        self.assertEqual(data.get("place"), "Набережная")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        """Тестирование удаления привычки."""

        url = reverse("habits:habit-delete", args=(self.habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тестирование вывода списка привычек."""
        url = reverse("habits:habit-list")

        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "user": 3,
                    "place": "Парк",
                    "time": "07:00",
                    "action": "Бегать",
                    "periodicity": 1,
                    "pleasant_habit": 3,
                    "reward": None,
                    "time_to_complete": 120,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class PleasantHabitTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email="tester@sky.pro")
        self.pleasant_habit = PleasantHabit.objects.create(user=self.user, action="Ванна с пеной", is_pleasant=True)
        self.client.force_authenticate(user=self.user)

    def test_pleasant_habit_retrieve(self):
        """Тестирование просмотра приятной привычки."""
        url = reverse("habits:pleasant-habit-detail", args=(self.pleasant_habit.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.pleasant_habit.action)

    def test_pleasant_habit_create(self):
        """Тестирование создания приятной привычки."""
        url = reverse("habits:pleasant-habit-create")
        data = {"action": "Ходить на массаж", "is_pleasant": True}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PleasantHabit.objects.all().count(), 2)

    def test_pleasant_habit_update(self):
        """Тестирование изменения приятной привычки."""

        url = reverse("habits:pleasant-habit-edit", args=(self.pleasant_habit.pk,))
        data = {"action": "Ходить на массаж стоп"}
        response = self.client.patch(url, data)

        self.assertEqual(data.get("action"), "Ходить на массаж стоп")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pleasant_habit_delete(self):
        """Тестирование удаления приятной привычки."""

        url = reverse("habits:pleasant-habit-delete", args=(self.pleasant_habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PleasantHabit.objects.all().count(), 0)

    def test_pleasant_habit_list(self):
        """Тестирование вывода списка приятных привычек."""
        url = reverse("habits:pleasant-habit-list")

        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{"id": 9, "user": 8, "action": "Ванна с пеной", "is_pleasant": True}],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
