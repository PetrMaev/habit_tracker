from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from users.permissions import IsModer, IsUserOwner
from users.serializers import CustomUserSerializer, CustomUserCreateSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = CustomUserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]


class UserListAPIView(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]
