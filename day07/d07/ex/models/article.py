from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    synopsis = models.CharField(max_length=312, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return str(self.title)
