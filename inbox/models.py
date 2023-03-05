from django.db import models
from user.models import User

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_inbox')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


class Inbox(models.Model):
    sender = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE)
    messages = models.ManyToManyField(Message, through='InboxMessage')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read_at = models.DateTimeField(null=True, blank=True)


class InboxMessage(models.Model):
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
