# Generated by Django 4.0.4 on 2022-07-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurDailyPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlaceName', models.CharField(max_length=50)),
                ('Descriptoon', models.TextField(max_length=2000)),
                ('Photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OurPartners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parntername', models.CharField(max_length=50)),
                ('Logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
