from rest_framework import fields
from api.models import Comment, Post, PostImage
from accounts.serializers import UserSerializer
from rest_framework import serializers


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
        # fields = ["images"]

    def get_images(self, obj):
        print("ysseo", obj)
        qs = PostImage.objects.filter(post=obj).all()
        serializer = PostImageSerializer(qs, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = "__all__"

