# Generated by Django 3.2.18 on 2023-03-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0009_alter_rental_returndate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='FinishedRent',
            field=models.BooleanField(default=0),
        ),
    ]
