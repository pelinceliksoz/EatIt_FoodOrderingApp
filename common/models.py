from django.db import models
from restaurantApp.models import Restaurant

class Food(models.Model):
    food_name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    price = models.FloatField(null=0)
    description = models.CharField(max_length=80, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.food_name
