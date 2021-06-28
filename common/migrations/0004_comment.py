# Generated by Django 3.2.4 on 2021-06-23 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_operations', '0001_initial'),
        ('common', '0003_auto_20210623_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('content', models.CharField(max_length=1000, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_operations.customer')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.food')),
            ],
        ),
    ]