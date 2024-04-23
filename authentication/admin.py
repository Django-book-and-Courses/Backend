from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.contrib import admin
from .models import CustomUser, UserProfile


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


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "get_picture", "bio")  # Display fields in the list view
    search_fields = (
        "user__email",
        "user__username",
    )  # Enable searching by user's email

    def get_picture(self, obj):
        if obj.picture:
            return format_html(
                '<img src="{}" width="40" style="border-radius: 50%;">',
                obj.picture.url,
            )
        else:
            return None

    get_picture.short_description = "Picture"  # Set column header for the picture field

    fieldsets = (
        (None, {"fields": ("user",)}),
        ("Profile Info", {"fields": ("bio", "picture")}),
    )  # Group fields in the add/edit form

    readonly_fields = ("user", "get_picture")  # Make user and picture read-only

    list_filter = (
        "user__is_active",
        "user__is_staff",
    )  # Add filters for user's active status and staff status


admin.site.register(UserProfile, UserProfileAdmin)
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
