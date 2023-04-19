# Generated by Django 4.1.7 on 2023-03-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0005_alter_processor_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processor',
            options={'ordering': ('Name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='processor',
            name='Cores',
            field=models.IntegerField(verbose_name='Ядра'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Frequency',
            field=models.CharField(max_length=10, verbose_name='Частота'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Graphics_core',
            field=models.CharField(blank=True, default=None, max_length=40, verbose_name='Графическое ядро'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Heat_dissipation',
            field=models.IntegerField(verbose_name='Теплоотдача'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Max_RAM_frequency',
            field=models.IntegerField(verbose_name='Максимальная частота оперативки'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Memory_type',
            field=models.CharField(choices=[('DDR3', 'DDR3'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=4, verbose_name='Тип памяти'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Name',
            field=models.CharField(max_length=40, verbose_name='Наименоваие'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Photo',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='processor',
            name='Socket',
            field=models.CharField(choices=[('AM4', 'AM4'), ('AM3+', 'AM3+'), ('AM5', 'AM5'), ('LGA 1151', 'LGA 1151'), ('LGA 1200', 'LGA 1200'), ('LGA 1700', 'LGA 1700'), ('LGA 2066', 'LGA 2066')], default='LGA 1151', max_length=8, verbose_name='Сокет'),
        ),
    ]
