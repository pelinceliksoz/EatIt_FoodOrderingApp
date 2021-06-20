# Generated by Django 3.2.4 on 2021-06-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurantApp', '0002_restaurant_restaurant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=80)),
                ('category', models.CharField(max_length=80)),
                ('price', models.FloatField(null=0)),
                ('description', models.CharField(max_length=80, null=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurantApp.restaurant')),
            ],
        ),
    ]