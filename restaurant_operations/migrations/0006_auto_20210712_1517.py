# Generated by Django 3.2.4 on 2021-07-12 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_operations', '0005_restaurant_ordered_food_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='avg_food_price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rate',
        ),
    ]
