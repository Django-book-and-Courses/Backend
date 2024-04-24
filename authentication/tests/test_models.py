from django.test import TestCase
from ..models import CustomUser

class CustomUserModelTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword'
        )

    def test_custom_user_creation(self):
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.profile.bio, None)
