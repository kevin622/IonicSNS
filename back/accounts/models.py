from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(to='self', related_name='followings', symmetrical=False)