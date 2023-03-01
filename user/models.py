from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password



class CustomUserManager(BaseUserManager):
    def create_user(self, user_name, password=None, **extra_fields):
        if not user_name:
            raise ValueError('The Username field must be set')
        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password=None, **extra_fields):
        return self.create_user(user_name, password, **extra_fields)


    
class User(AbstractBaseUser):
    last_login = None
    is_staff = models.BooleanField(default=True)
    user_name = models.CharField(unique=True,max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, blank=True, null=True, default="")
    bio = models.TextField(max_length=2000, blank=True, null=True , default="")
    website = models.URLField(max_length=300,blank=True, null=True)
    phone_number = models.CharField(max_length=30, null=True,blank=True)
    profile_pic_url = models.ImageField(upload_to='static/images/avatar/', null=True, blank= True)
    cover_pic_url = models.ImageField(upload_to='static/images/cover/', null=True, blank= True)
    
    USERNAME_FIELD = 'user_name'
    
    objects = CustomUserManager()
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.user_name
    
