# Generated by Django 4.2.5 on 2023-11-07 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0014_alter_rooms_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='description',
            field=models.TextField(),
        ),
    ]
