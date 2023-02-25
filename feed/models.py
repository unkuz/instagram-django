from django.db import models
from user.models import User


class Image(models.Model):
    src = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    src = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    text = models.TextField(max_length=5000, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


class Feed(models.Model):
    caption_text = models.TextField(max_length=5000, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, through='FeedImage')
    videos = models.ManyToManyField(Video, through='FeedVideo')

    likes = models.ManyToManyField(
        User, through='FeedLike', related_name='feed_like')

    save = models.ManyToManyField(
        User, through='FeedSave', related_name='feed_save')

    comments = models.ManyToManyField(
        Comment, through='FeedComment', related_name='feed_comment')

    def __str__(self):
        return self.caption_text


class FeedImage(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class FeedVideo(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class FeedLike(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FeedSave(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FeedComment(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
