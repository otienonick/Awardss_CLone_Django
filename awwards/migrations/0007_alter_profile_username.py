# Generated by Django 3.2.8 on 2021-10-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0006_auto_20211023_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]