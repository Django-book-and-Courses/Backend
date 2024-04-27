from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework import status
from ..views import UserProfileViewSet
from ..models import CustomUser


class AuthViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )

    def test_register(self):
        url = reverse("auth-register")
        data = {
            "email": "test2@example.com",
            "username": "testuser2",
            "password": "testpassword",
            "password_confirm": "testpassword",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_password_mismatch(self):
        url = reverse("auth-register")
        data = {
            "email": "test2@example.com",
            "username": "testuser2",
            "password": "testpassword",
            "password_confirm": "testpassword2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(), {"non_field_errors": ["The passwords do not match."]}
        )

    def test_register_used_username(self):
        url = reverse("auth-register")
        data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword",
            "password_confirm": "testpassword",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(), {"username": ["A user with that username already exists."]}
        )

    def test_register_used_email(self):
        url = reverse("auth-register")
        data = {
            "email": "test@example.com",
            "username": "testuser2",
            "password": "testpassword",
            "password_confirm": "testpassword",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(), {"email": ["A user with that email already exists."]}
        )

    def test_register_no_data(self):
        url = reverse("auth-register")
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json(),
            {
                "username": ["This field is required."],
                "email": ["This field is required."],
                "password": ["This field is required."],
                "password_confirm": ["This field is required."],
            },
        )

    def test_login(self):
        url = reverse("auth-login")
        data = {"email": "test@example.com", "password": "testpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid(self):
        url = reverse("auth-login")
        data = {"email": "invalid@example.com", "password": "invalidpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {"error": "Invalid credentials"})

    def test_login_no_data(self):
        url = reverse("auth-login")
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {"error": "Invalid credentials"})

    def test_logout(self):
        url = reverse("auth-logout")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Logout successful"})

        # Attempt to access an authenticated endpoint after logout
        profile_url = reverse("profile-detail")
        profile_response = self.client.get(profile_url)

        # Verify that the response is Forbidden (403) or redirected to the login page
        self.assertIn(
            profile_response.status_code,
            [status.HTTP_403_FORBIDDEN, status.HTTP_302_FOUND],
        )


class UserProfileViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_profile_get(self):
        url = reverse("profile-detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_get_not_authenticated(self):
        url = reverse("profile-detail")
        request = self.factory.get(url)
        response = UserProfileViewSet.as_view({"get": "get_profile_by_username"})(
            request
        )
        response.render()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.content, b'{"detail":"Authentication credentials were not provided."}'
        )

    def test_profile_get_by_username(self):
        url = reverse("get-profile-by-username", args=["testuser"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_get_by_username_invalid(self):
        url = reverse("get-profile-by-username", args=["testuserasd"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"error": "Profile not found"})

    def test_profile_partial_update(self):
        url = reverse("profile-detail")
        data = {"first_name": "John"}

        # Check the initial state of the profile
        initial_response = self.client.get(url)
        initial_data = initial_response.json()
        initial_first_name = initial_data["first_name"]

        # Perform the partial update
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the profile was updated successfully
        updated_response = self.client.get(url)
        updated_data = updated_response.json()
        updated_first_name = updated_data["first_name"]
        self.assertNotEqual(initial_first_name, updated_first_name)
        self.assertEqual(updated_first_name, "John")

    def test_profile_partial_update_not_authenticated(self):
        url = reverse("profile-detail")
        request = self.factory.put(url)
        response = UserProfileViewSet.as_view({"put": "partial_update"})(
            request
        )
        response.render()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.content, b'{"detail":"Authentication credentials were not provided."}'
        )