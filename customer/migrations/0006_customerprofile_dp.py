# Generated by Django 3.2.18 on 2023-03-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20230221_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='dp',
            field=models.ImageField(null=True, upload_to='media/dp/'),
        ),
    ]