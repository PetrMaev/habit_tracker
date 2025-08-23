from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderators").exists()


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем привычки."""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False


class IsUserOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем своего профиля."""

    def has_object_permission(self, request, view, obj):
        if obj.email == request.user.email:
            return True
        return False
