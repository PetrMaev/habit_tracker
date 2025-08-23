from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit, PleasantHabit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer, PleasantHabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)  # noqa: F841


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.filter(user=self.request.user):
            return queryset
        else:
            return queryset.filter(is_public=True)


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


# Pleasant habits
class PleasantHabitCreateAPIView(generics.CreateAPIView):
    serializer_class = PleasantHabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pleasant_habit = serializer.save(user=self.request.user)  # noqa: F841


class PleasantHabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PleasantHabitListAPIView(generics.ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.groups.filter(name="Moderators").exists():
            return queryset
        else:
            return queryset.filter(user=self.request.user)


class PleasantHabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PleasantHabitDestroyAPIView(generics.DestroyAPIView):
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
