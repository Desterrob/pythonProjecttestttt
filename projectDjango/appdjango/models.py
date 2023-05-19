from django.db import models
class teste(models.Model):
    nome = models.CharField(
        max_length=100
    )