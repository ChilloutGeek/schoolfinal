# Generated by Django 3.2.18 on 2023-03-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_customerprofile_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='dp',
            field=models.ImageField(null=True, upload_to='dp/'),
        ),
    ]
