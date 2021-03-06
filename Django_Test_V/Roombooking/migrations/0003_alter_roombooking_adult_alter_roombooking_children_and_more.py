# Generated by Django 4.0.4 on 2022-07-19 02:08

import Roombooking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roombooking', '0002_adultfield_bedtypefield_childrenfield_roomtypefield_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='Adult',
            field=models.CharField(blank=True, choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Children',
            field=models.CharField(blank=True, choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Rate',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Adultfield',
        ),
        migrations.DeleteModel(
            name='Childrenfield',
        ),
    ]
