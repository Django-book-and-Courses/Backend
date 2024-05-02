from typing import Any
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.backends import ModelBackend


class CustomBackends(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        try:
            User = get_user_model()
            user = User.objects.filter(username=username)
        except user.DoesNotExist:
            return
        
        if user.exists():
            my_user = user.first()
            if my_user.check_password(password):
                return my_user
            return
        return