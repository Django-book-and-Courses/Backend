from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, verbose_name="User", on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(
        upload_to="profile_pictures", default="profile_pictures/default.jpg"
    )


# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self._create_user(email, password, **extra_fields)

# class Users(AbstractUser):
#     username = models.CharField(max_length=150, blank=True, null=True)
#     email = models.EmailField(unique=True)
#     photo_user = models.ImageField(upload_to='photos/profile', blank=True, null=True)
#     gender = models.CharField(max_length=20)
#     phone = models.CharField(max_length=16)
#     address = models.CharField(max_length=150)

#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'username'

#     # objects = UserManager()

#     def __str__(self):
#         return self.email

#     class Meta:
#         verbose_name_plural = 'Users'
