# Generated by Django 3.2.4 on 2021-06-16 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.usermodel')),
                ('rate', models.IntegerField(null=0)),
                ('category', models.CharField(max_length=80, null=True)),
            ],
        ),
    ]
