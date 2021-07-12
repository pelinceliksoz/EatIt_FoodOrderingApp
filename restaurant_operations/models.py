from django.db import models
from accounts.models import CustomUser


class Restaurant(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    restaurant_name = models.CharField(max_length=80, null=True)
    category = models.CharField(max_length=80, null=True)
    avg_int_food_price = models.IntegerField(null=True)
    ordered_food_count = models.IntegerField(null=True)

    def __str__(self):
        return self.user.user.username

