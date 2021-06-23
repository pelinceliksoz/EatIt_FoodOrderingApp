from django.db import models
from restaurant_operations.models import Restaurant
from customer_operations.models import Customer


class Food(models.Model):
    food_name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    price = models.FloatField(null=0)
    description = models.CharField(max_length=80, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(Customer, related_name='restaurant_foods')
    orders = models.ManyToManyField(Customer, related_name='order_foods')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.food_name
