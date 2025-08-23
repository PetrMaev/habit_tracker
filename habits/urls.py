from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PleasantHabitCreateAPIView, PleasantHabitDestroyAPIView,
                          PleasantHabitListAPIView, PleasantHabitRetrieveAPIView, PleasantHabitUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("habits/list/", HabitListAPIView.as_view(), name="habit-list"),
    path("habits/<int:pk>/edit/", HabitUpdateAPIView.as_view(), name="habit-edit"),
    path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit-delete"),
    path("pleasant_habit/create/", PleasantHabitCreateAPIView.as_view(), name="pleasant-habit-create"),
    path("pleasant_habit/<int:pk>/", PleasantHabitRetrieveAPIView.as_view(), name="pleasant-habit-detail"),
    path("pleasant_habit/list/", PleasantHabitListAPIView.as_view(), name="pleasant-habit-list"),
    path("pleasant_habit/<int:pk>/edit/", PleasantHabitUpdateAPIView.as_view(), name="pleasant-habit-edit"),
    path("pleasant_habit/<int:pk>/delete/", PleasantHabitDestroyAPIView.as_view(), name="pleasant-habit-delete"),
]
