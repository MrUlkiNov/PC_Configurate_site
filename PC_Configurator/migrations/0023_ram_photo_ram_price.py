# Generated by Django 4.1.7 on 2023-03-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0022_ram'),
    ]

    operations = [
        migrations.AddField(
            model_name='ram',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='ram',
            name='Price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
