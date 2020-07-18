from api.views import CommentViewSet, PostViewSet
from django.urls import path, include
from accounts.views import ProfileViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register(r"posts/(?P<post_pk>\d+)/comments", CommentViewSet)


urlpatterns = [path("", include(router.urls))]

