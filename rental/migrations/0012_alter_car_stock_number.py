# Generated by Django 3.2.18 on 2023-03-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0011_car_stock_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Stock_Number',
            field=models.IntegerField(default=0, null=True),
        ),
    ]