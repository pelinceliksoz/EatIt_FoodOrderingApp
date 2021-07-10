from django.db import models
from accounts.models import CustomUser


class Restaurant(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    rate = models.IntegerField(null=0)
    restaurant_name = models.CharField(max_length=80, null=True)
    category = models.CharField(max_length=80, null=True)
    avg_food_price = models.FloatField(null=True)
    avg_int_food_price = models.IntegerField(null=0)

    def __str__(self):
        return self.user.user.username

