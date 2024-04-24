from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ["picture", "bio"]


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)
    password_confirm = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = models.CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "profile",
            "password",
            "password_confirm",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def __init__(self, *args, **kwargs):
        self.is_register = kwargs.pop("is_register", False)
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        if self.is_register and attrs["password"] != attrs.pop("password_confirm"):
            raise serializers.ValidationError("The passwords do not match.")
        return super().validate(attrs)

    def create(self, validated_data):
        profile_data = validated_data.pop("profile", None)
        email = validated_data.get("email")
        if email and models.CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ["A user with that email already exists."]}
            )
        user = models.CustomUser.objects.create_user(**validated_data)
        if profile_data:
            models.UserProfile.objects.create(user=user, **profile_data)
        return user


    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", None)
        instance = super().update(instance, validated_data)
        if profile_data:
            profile_serializer = self.fields["profile"]
            profile_instance = instance.profile
            profile_serializer.update(profile_instance, profile_data)
        return instance


class EmptySerializer(serializers.Serializer):
    pass
