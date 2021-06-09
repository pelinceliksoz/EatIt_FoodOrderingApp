from django.db import models

# Create your models here.

class Restaurant(models.Model):
    restId = models.IntegerField(),
    name = models.CharField(max_length=100)


