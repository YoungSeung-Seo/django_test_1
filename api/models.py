from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStampField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(TimeStampField):
    LANG_CHOICES = [
        ("kor", "Korean"),
        ("jpn", "Japanese"),
        ("eng", "English"),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_url = models.URLField()
    image_urls = models.ManyToManyField("PostImage")
    lang = models.CharField(choices=LANG_CHOICES, default="kor")


class PostImage(models.Model):
    image = models.ImageField()


class Comment(TimeStampField):
    pass


class Tag(models.Model):
    pass

