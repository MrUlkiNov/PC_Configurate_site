# Generated by Django 4.1.7 on 2023-03-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0021_alter_videocard_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Memory_type', models.CharField(blank=True, choices=[('DDR3', 'DDR3'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=4, null=True, verbose_name='Тип памяти')),
                ('Memory', models.IntegerField(verbose_name='Количество памяти')),
                ('Max_frequency', models.IntegerField(verbose_name='Частота')),
            ],
            options={
                'verbose_name': 'Оперативная память',
                'verbose_name_plural': 'Оперативная память',
                'ordering': ('Name',),
            },
        ),
    ]