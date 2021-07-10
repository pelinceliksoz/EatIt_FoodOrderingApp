from django.db import models
from restaurant_operations.models import Restaurant
from customer_operations.models import Customer
from datetime import datetime


class Food(models.Model):
    food_name = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    price = models.FloatField(null=0)
    description = models.CharField(max_length=8000, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(Customer, related_name='restaurant_foods')
    orders = models.ManyToManyField(Customer, related_name='order_foods')
    food_pic = models.ImageField()
    rate = models.IntegerField(null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.food_name


class Comment(models.Model):
    date = models.DateField(default=datetime.now, null=True)
    content = models.CharField(max_length=8000, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    date = models.DateTimeField(default=datetime.now, null=True)
    message = models.TextField(max_length=8000, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

