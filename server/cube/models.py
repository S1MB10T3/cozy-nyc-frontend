from django.db import models
from django.contrib.auth.models import User


class Cube(models.Model):
    """This is a model for post/articles

    ToDo:
        Add CRUD
    """

    title = models.CharField(max_length=255, null=True, blank=True, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(max_length=1000, null=True, blank=True)
    article = models.TextField(max_length=15000, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
