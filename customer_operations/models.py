from django.db import models
from accounts.models import CustomUser


class Customer(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    address = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.user.user.username