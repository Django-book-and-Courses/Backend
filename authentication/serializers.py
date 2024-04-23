from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["picture", "bio"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(read_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = models.CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "userprofile",
            "password",
            "password_confirm",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("password_confirm"):
            raise serializers.ValidationError("The passwords do not match.")
        return super().validate(attrs)

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(**validated_data)
        return user


class EmptySerializer(serializers.Serializer):
    pass