from django.db import models
from user.models import User
from django.core.validators import FileExtensionValidator


class Image(models.Model):
    src = models.ImageField(upload_to='static/images/feed', null=True, blank=True,
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Video(models.Model):
    src = models.FileField(
        upload_to='static/videos/feed', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['.mp4', '.avi', '.mov'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentReply(models.Model):
    text = models.TextField(max_length=5000, default="")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feed_comment_reply_user')
    comment = models.ForeignKey(
        'Comment', on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField(max_length=5000, default="")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feed_comment_user')
    reply = models.ManyToManyField(
        CommentReply, through='CommentCommentReply', related_name='feed_replies')
    created_at = models.DateTimeField(auto_now_add=True)


class CommentCommentReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment_reply = models.ForeignKey(CommentReply, on_delete=models.CASCADE)


class Tag(models.Model):
    tag = models.CharField(max_length=50)


class Feed(models.Model):
    caption_text = models.TextField(max_length=5000, null=False, blank=False)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feed_user')

    images = models.ManyToManyField(Image, through='FeedImage')
    videos = models.ManyToManyField(Video, through='FeedVideo')

    likes = models.ManyToManyField(
        User, through='FeedLike', related_name='feed_like')

    saved = models.ManyToManyField(
        User, through='FeedSave', related_name='feed_save')

    comments = models.ManyToManyField(
        Comment, through='FeedComment', related_name='feed_comment')

    tags = models.ManyToManyField(
        Tag, through='FeedTag', related_name='feed_tag')

    seen = models.ManyToManyField(
        User, through='FeedSeen', related_name='feed_seen')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


class FeedTag(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class FeedSeen(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
