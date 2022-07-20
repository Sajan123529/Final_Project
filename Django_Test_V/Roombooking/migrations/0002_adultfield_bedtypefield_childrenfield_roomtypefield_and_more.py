# Generated by Django 4.0.4 on 2022-07-19 01:33

import Roombooking.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Roombooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adultfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BedTypefield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Childrenfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomTypefield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Rate', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Rate',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Adult',
            field=models.ForeignKey(blank=True, choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')], null=True, on_delete=django.db.models.deletion.CASCADE, to='Roombooking.adultfield'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Bed_type',
            field=models.ForeignKey(blank=True, choices=[('Queen Size Bed', 'Queen Size Bed'), ('Deluxe Bed', 'Deluxe Bed'), ('Normal Bed', 'Normal Bed'), ('Double Bed', 'Double Bed'), ('Single Bed', 'Single Bed')], null=True, on_delete=django.db.models.deletion.CASCADE, to='Roombooking.bedtypefield'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Children',
            field=models.ForeignKey(blank=True, choices=[('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')], null=True, on_delete=django.db.models.deletion.CASCADE, to='Roombooking.childrenfield'),
        ),
        migrations.AlterField(
            model_name='roombooking',
            name='Room_Type',
            field=models.ForeignKey(blank=True, choices=[('with bathroom', 'with bathroom'), ('without bathroom', 'without bathroom'), ('deluxe room', 'deluxe room'), ('super deluxe room', 'super deluxe room'), ('normal room', 'normal room')], null=True, on_delete=django.db.models.deletion.CASCADE, to='Roombooking.roomtypefield'),
        ),
    ]
