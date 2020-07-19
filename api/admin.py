from django.contrib import admin
from api.models import Post, PostAudio, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 1


class PostAudioAdmin(admin.TabularInline):
    model = PostAudio
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin, PostAudioAdmin]

    class Meta:
        model = Post


# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass


# @admin.register(PostAudio)
# class PostAudioAdmin(admin.ModelAdmin):
#     pass
