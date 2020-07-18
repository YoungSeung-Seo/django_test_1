from rest_framework import viewsets
from api.serializers import CommentSerializer, PostSerializer
from api.models import Comment, Post
from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(post__pk=self.kwargs.get("post_pk"))
        return qs

