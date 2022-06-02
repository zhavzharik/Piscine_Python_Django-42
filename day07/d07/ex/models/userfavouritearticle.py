from django.contrib.auth.models import User
from django.db import models
from . import Article


class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.article.title)
