from django.test import TestCase
from django.conf import settings
from ..models import CustomUser, UserProfile
from ..serializers import UserSerializer, UserProfileSerializer


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser1", email="test1@example.com", password="testpassword"
        )

    def test_user_serializer(self):
        serializer = UserSerializer(instance=self.user)
        expected_data = {
            "id": self.user.id,
            "username": "testuser1",
            "first_name": "",
            "last_name": "",
            "profile": {
                "picture": settings.DEFALUT_PROFILE_IMAGE_PATH,
                "bio": None,
            }
        }
        self.assertEqual(serializer.data, expected_data)


class UserProfileSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser2", email="test2@example.com", password="testpassword"
        )

    def test_user_profile_serializer(self):
        serializer = UserProfileSerializer(instance=self.user.profile)
        expected_data = {
            "picture": settings.DEFALUT_PROFILE_IMAGE_PATH,
            "bio": None,
        }
        self.assertEqual(serializer.data, expected_data)
