# Generated by Django 3.2.4 on 2021-07-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_alter_food_food_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]