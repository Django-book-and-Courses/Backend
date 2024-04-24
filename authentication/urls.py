from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r"auth", AuthViewSet, basename="auth")
# router.register(r"profile", UserProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "profile",
        UserProfileViewSet.as_view(
            {"get": "get_profile", "patch": "partial_update"}
        ),
        name="profile-detail",
    ),
    path(
        "profile/<str:username>",
        UserProfileViewSet.as_view({"get": "get_profile_by_username"}),
        name="get-profile-by-username",
    ),
]
