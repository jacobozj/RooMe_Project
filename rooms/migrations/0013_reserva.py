# Generated by Django 4.1.11 on 2023-10-29 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_users_profile'),
        ('rooms', '0012_rooms_available_bedrooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField(auto_now_add=True)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.rooms')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
        ),
    ]
