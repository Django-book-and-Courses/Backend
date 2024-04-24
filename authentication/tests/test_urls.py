from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import AuthViewSet, UserProfileViewSet

class TestUrls(SimpleTestCase):
    def test_auth_register_url_resolves(self):
        url = reverse('auth-register')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.cls, AuthViewSet)

    def test_auth_login_url_resolves(self):
        url = reverse('auth-login')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.cls, AuthViewSet)

    def test_auth_logout_url_resolves(self):
        url = reverse('auth-logout')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.cls, AuthViewSet)

    def test_profile_detail_url_resolves(self):
        url = reverse('profile-detail')
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.cls, UserProfileViewSet)

    def test_get_profile_by_username_url_resolves(self):
        url = reverse('get-profile-by-username', args=['testuser'])
        resolved_func = resolve(url).func
        self.assertEqual(resolved_func.cls, UserProfileViewSet)
