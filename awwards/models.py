from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 255,unique=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...',max_length=300)
    avatar = models.ImageField(default='avatar.png',upload_to = 'avatars/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}-{self.created}'