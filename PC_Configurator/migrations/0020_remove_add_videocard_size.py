# Generated by Django 4.1.7 on 2023-03-19 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0019_add_videocard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_videocard',
            name='Size',
        ),
    ]
