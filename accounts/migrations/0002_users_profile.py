# Generated by Django 4.1.11 on 2023-09-26 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile',
            field=models.CharField(default='estudiante', max_length=15),
        ),
    ]
