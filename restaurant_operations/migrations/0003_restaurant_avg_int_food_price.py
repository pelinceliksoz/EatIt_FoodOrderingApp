# Generated by Django 3.2.4 on 2021-07-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_operations', '0002_restaurant_avg_food_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='avg_int_food_price',
            field=models.IntegerField(default=0, null=0),
            preserve_default=False,
        ),
    ]