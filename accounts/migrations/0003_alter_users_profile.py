# Generated by Django 4.1.11 on 2023-09-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile',
            field=models.CharField(max_length=15),
        ),
    ]