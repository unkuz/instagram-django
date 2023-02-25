from django.db import models
from user.models import User


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feed(models.Model):
    text = models.TextField(max_length=5000, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, through='FeedImage')
    videos = models.ManyToManyField(Video, through='FeedVideo')

    def __str__(self):
        return self.text


class FeedImage(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class FeedVideo(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
