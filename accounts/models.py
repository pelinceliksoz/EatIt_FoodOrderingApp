from django.db import models
from django.contrib.auth.models import User, auth


class UserModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = models.IntegerField()
    location = models.CharField(max_length=80)

    def __str__(self):
        return self.user.username
