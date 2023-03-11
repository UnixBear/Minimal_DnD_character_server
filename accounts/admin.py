from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "favorite_class",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("favorite_class",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("favorite_class",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
