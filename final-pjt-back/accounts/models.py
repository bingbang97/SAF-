from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    like_genre1 = models.CharField(max_length=50)
    like_genre2 = models.CharField(max_length=50)
    like_genre3 = models.CharField(max_length=50)