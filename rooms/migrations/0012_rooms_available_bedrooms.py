# Generated by Django 4.1.11 on 2023-10-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_rooms_renter_alter_rooms_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='available_bedrooms',
            field=models.IntegerField(default=0),
        ),
    ]
