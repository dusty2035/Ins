from django.db import models
from user.models import CustomUser
# Create your models here.

class Post(models.Model):
    picture = models.ImageField(upload_to='images/')
    caption = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)