# Generated by Django 3.2.4 on 2021-07-01 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]