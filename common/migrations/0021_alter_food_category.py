# Generated by Django 3.2.4 on 2021-08-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_auto_20210712_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Fast Food', 'Fast Food'), ('Pastry', 'Pastry'), ('Meat', 'Meat'), ('Chicken', 'Chicken'), ('Fish', 'Fish'), ('Healthy', 'Healthy'), ('Sweet', 'Sweet'), ('Drink', 'Drink')], max_length=200, null=True),
        ),
    ]
