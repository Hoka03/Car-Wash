# Generated by Django 5.0.7 on 2024-07-19 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pricing', '0001_initial'),
        ('washing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='car_wash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='washing.carwash'),
        ),
        migrations.AddField(
            model_name='pricing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='washing.category'),
        ),
        migrations.AlterUniqueTogether(
            name='pricing',
            unique_together={('car_model', 'category', 'car_wash')},
        ),
    ]
