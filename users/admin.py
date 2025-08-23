from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "avatar", "phone_number", "country", "tg_chat_id")
    search_fields = ("email",)
