# Generated by Django 3.2.8 on 2021-10-23 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0005_auto_20211023_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='created',
        ),
        migrations.RemoveField(
            model_name='like',
            name='updated',
        ),
    ]