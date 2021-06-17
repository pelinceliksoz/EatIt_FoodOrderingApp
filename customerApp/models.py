from django.db import models
from accounts.models import UserModel

class Customer(models.Model):
    user=models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    address = models.CharField(max_length=400, null=True)
    def __str__(self):
        return self.user.user.username