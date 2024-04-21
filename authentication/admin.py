from .models import Users
from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import admin as django_admin

@admin.register(Users)
class UserAdmin(django_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    list_display = ("email", "username", "gender", "is_active", "is_staff")
    fieldsets = django_admin.UserAdmin.fieldsets + (
        (
            "Personal Info",
            {
                "fields": ("photo_user", "gender", "phone", "address", "date_of_birth"),
            },
        ),
    )