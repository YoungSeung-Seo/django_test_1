from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.decorators import action
from accounts.serializers import ProfileSerializer, UserSerializer, serializers
from accounts.models import Profile
from rest_framework import viewsets
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["GET"], url_path="detail")
    def user_detail(self, request, pk):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data, status=status.HTTP_303_SEE_OTHER)

    @action(detail=True, methods=["PATCH"])
    def reset_email(self, request, pk):
        instance = self.get_object()
        instance.email = ""
        instance.save(update_fields=["email"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
