# Generated by Django 4.1.7 on 2023-03-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_Configurator', '0010_delete_add_processor'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
    ]
