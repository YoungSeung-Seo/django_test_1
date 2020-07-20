from django.urls import path, include
from accounts.views import ProfileViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

router = DefaultRouter()
router.register("profile", ProfileViewSet)
router.register("user", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", obtain_jwt_token),
    path("api-token-refresh/", refresh_jwt_token),
    path("api-token-verify/", verify_jwt_token),
]

