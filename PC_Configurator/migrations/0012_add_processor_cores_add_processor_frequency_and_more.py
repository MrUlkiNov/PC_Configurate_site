# Generated by Django 4.1.7 on 2023-03-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0011_add_processor'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_processor',
            name='Cores',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ядра'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Frequency',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Частота'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Graphics_core',
            field=models.CharField(blank=True, default='Не имеется', max_length=40, null=True, verbose_name='Графическое ядро'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Heat_dissipation',
            field=models.IntegerField(blank=True, null=True, verbose_name='Теплоотдача'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Max_RAM_frequency',
            field=models.IntegerField(blank=True, null=True, verbose_name='Максимальная частота оперативки'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Memory_type',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Тип памяти'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='add_processor',
            name='Socket',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Сокет'),
        ),
    ]
