from django.db import models
from user.models import User



class Feed(models.Model):
    text = models.TextField(max_length=5000,default="")
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    