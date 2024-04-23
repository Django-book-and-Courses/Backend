from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)

# @admin.register(Users)
# class UserAdmin(django_admin.UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     model = Users
#     list_display = ("email", "username", "gender", "is_active", "is_staff")
#     fieldsets = django_admin.UserAdmin.fieldsets + (
#         (
#             "Personal Info",
#             {
#                 "fields": ("photo_user", "gender", "phone", "address", "date_of_birth"),
#             },
#         ),
#     )
