from django.db import models
from accounts.models import UserModel

class Customer(models.Model):
    user=models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.user.user.username