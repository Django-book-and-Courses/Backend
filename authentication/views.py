from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from . import serializers, models
import pyotp


class AuthViewSet(ViewSet):
    # serializer_class = serializers.UserSerializer

    @action(detail=False, methods=["POST"])
    def register(self, request):
        serializer = serializers.UserSerializer(data=request.data, is_register=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["POST"])
    def login(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        code = request.data.get("code")

        user = authenticate(request, email=email, password=password)

        if user:
            # ? totp login
            if user.is_totp:
                if not code:
                    return Response(
                        {"error": 'Invalid Form Body ["code is required"]'},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                totp = pyotp.TOTP(user.totp_secret)
                if totp.at(request.timestamp) != code:
                    return Response(
                        {"error": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST
                    )

            # ? normal login
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

    @action(detail=False, methods=["POST"])
    def logout(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["POST"],
        url_path=r"mfa/totp/enable",
        url_name="mfa-enable-totp",
    )
    def enable_totp(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_403_FORBIDDEN,
            )
        secret = request.data.get("secret", None)
        code = request.data.get("code", None)
        user = request.user

        # ? check if there is code and secret
        if not (secret and code):
            return Response(
                {"error": "Invalid Form Body"}, status=status.HTTP_400_BAD_REQUEST
            )

        # ? check if totp already enabled
        if user.is_totp or user.totp_secret:
            return Response(
                {"error": "TOTP already enabled"}, status=status.HTTP_400_BAD_REQUEST
            )

        # ? check code length
        if len(code) < 6:
            return Response(
                {"error": f"Invalid Code Length {len(code)} Should be 6"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # ? check code
        totp = pyotp.TOTP(secret)
        if not totp.at(request.timestamp) != code:
            return Response(
                {"error": "Invalid two-factor code"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.is_totp = True
        user.totp_secret = secret
        user.save()
        return Response(
            {"message": "TOTP enabled successful"}, status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=["POST"],
        url_path=r"mfa/totp/disable",
        url_name="mfa-disable-totp",
    )
    def disable_totp(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_403_FORBIDDEN,
            )

        user = self.request.user
        if not user.is_totp:
            return Response(
                {"error": "TOTP already disabled"}, status=status.HTTP_400_BAD_REQUEST
            )

        user.is_totp = False
        user.totp_secret = None
        return Response(
            {"message": "TOTP disabled successful"}, status=status.HTTP_200_OK
        )


class UserProfileViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def get_profile(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_profile_by_username(self, request, username=None):
        try:
            user = models.CustomUser.objects.get(username=username)
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.CustomUser.DoesNotExist:
            return Response(
                {"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def partial_update(self, request):
        user = request.user
        serializer = serializers.UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
