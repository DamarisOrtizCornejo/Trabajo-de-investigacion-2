# Generated by Django 4.0.2 on 2022-03-18 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0004_alter_departamento_options_alter_empleado_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombre'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
