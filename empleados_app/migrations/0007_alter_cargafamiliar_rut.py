# Generated by Django 4.2.4 on 2023-12-09 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0006_alter_cargafamiliar_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargafamiliar',
            name='rut',
            field=models.CharField(max_length=15),
        ),
    ]
