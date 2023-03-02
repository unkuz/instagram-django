from django.db import models
from user.models import User
# Create your models here.


class Image(models.Model):
    src = models.ImageField(
        upload_to='static/images/story', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    src = models.FileField(
        upload_to='static/videos/story', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    tag = models.CharField(max_length=50)


class Comment(models.Model):
    text = models.TextField(max_length=5000, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="story_comments")
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


class Story(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, through='StoryImage',related_name='story_images')
    videos = models.ManyToManyField(Video, through='StoryVideo',related_name='story_videos')

    likes = models.ManyToManyField(
        User, through='StoryLike', related_name='story_like')

    saved = models.ManyToManyField(
        User, through='StorySave', related_name='story_save')

    comments = models.ManyToManyField(
        Comment, through='StoryComment', related_name='story_comment')

    tags = models.ManyToManyField(
        Tag, through='StoryTag', related_name='story_tag')
    
    seen = models.ManyToManyField(User,through='StorySeen', related_name='story_seen')

    def __str__(self):
        return self.caption_text


class StoryImage(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class StoryVideo(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class StorySave(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class StoryComment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class StoryTag(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class StoryLike(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class StorySeen(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)