from rest_framework import serializers
from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = [
            "id",
            "username",
            "email",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ["user", "bio", "location"]
        read_only_fields = ["user"]

