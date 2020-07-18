from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class TimeStampField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampField):
    LANG_CHOICES = [
        ("kor", "Korean"),
        ("jpn", "Japanese"),
        ("eng", "English"),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lang = models.CharField(max_length=3, choices=LANG_CHOICES, default="kor")
    title = models.CharField(max_length=100)
    content = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True)


class PostImage(TimeStampField):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="api/post/%Y/%m/%d")
    index_time = models.IntegerField(default=0)


class Comment(TimeStampField):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

