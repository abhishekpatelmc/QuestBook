# Generated by Django 4.1.7 on 2023-03-27 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_passengerdetail_delete_pessanger_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passengerdetail',
            name='dest_id',
        ),
    ]
