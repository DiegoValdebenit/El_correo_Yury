# Generated by Django 4.2.4 on 2023-12-09 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0004_alter_cargafamiliar_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactoemergencia',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='empleados_app.empleado'),
        ),
    ]
