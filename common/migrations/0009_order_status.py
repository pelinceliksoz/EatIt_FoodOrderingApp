# Generated by Django 3.2.4 on 2021-07-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
