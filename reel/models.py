from django.db import models
from user.models import User

# Create your models here.


class Video(models.Model):
    src = models.FileField(
        upload_to='static/videos/reel', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    text = models.TextField(max_length=5000, default="")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reel_comment_user')
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='reel_replies')


class Tag(models.Model):
    tag = models.CharField(max_length=50)


class Reel(models.Model):
    caption_text = models.TextField(max_length=5000, null=False, blank=False)
    test = models.TextField(max_length=200, null=True, blank=True)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reel_user')
    videos = models.ManyToManyField(
        Video, through='ReelVideo')

    likes = models.ManyToManyField(
        User, through='ReelLike', related_name='reel_like')

    saved = models.ManyToManyField(
        User, through='ReelSave', related_name='reel_save')

    comments = models.ManyToManyField(
        Comment, through='ReelComment', related_name='reel_comment')

    tags = models.ManyToManyField(
        Tag, through='ReelTag', related_name='reel_tag')

    seen = models.ManyToManyField(
        User, through='ReelSeen', related_name='reel_seen')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReelVideo(models.Model):
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class ReelLike(models.Model):
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ReelSave(models.Model):
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ReelComment(models.Model):
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class ReelTag(models.Model):
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class ReelSeen(models.Model):
    reel = models.ForeignKey(Reel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
