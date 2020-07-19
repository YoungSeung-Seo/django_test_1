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


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    index_time = models.DurationField(default=0)


class PostAudio(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    audio = models.ImageField(upload_to="audios/%Y/%m/%d")
    duration = models.DurationField()


class Comment(TimeStampField):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

