# Generated by Django 4.1.7 on 2023-03-26 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pessanger_detail',
            fields=[
                ('Trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('Trip_same_id', models.IntegerField(default=1)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=10)),
                ('Trip_date', models.DateField()),
                ('payment', models.IntegerField(default=50)),
                ('payment_currency', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=20)),
                ('pay_done', models.IntegerField(default=0)),
                ('dest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.detailed_desc')),
            ],
            options={
                'verbose_name_plural': 'Trip Details',
            },
        ),
    ]