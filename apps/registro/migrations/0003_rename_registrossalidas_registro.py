# Generated by Django 5.1 on 2024-09-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_rename_registros_registrossalidas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegistrosSalidas',
            new_name='Registro',
        ),
    ]
