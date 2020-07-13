from django.urls import path, include
from accounts.views import ProfileViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", ProfileViewSet)
router.register("user", UserViewSet)


urlpatterns = [path("", include(router.urls))]

