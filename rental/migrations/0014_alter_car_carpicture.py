# Generated by Django 3.2.18 on 2023-03-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0013_car_carpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='CarPicture',
            field=models.ImageField(blank=True, upload_to='cars/'),
        ),
    ]