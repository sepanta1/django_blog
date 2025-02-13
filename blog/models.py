from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = User()

# Create your models here.
