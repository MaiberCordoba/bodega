# Generated by Django 5.1 on 2024-09-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_rename_registrossalidas_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='fechaIngreso',
            field=models.DateField(auto_now=True),
        ),
    ]
