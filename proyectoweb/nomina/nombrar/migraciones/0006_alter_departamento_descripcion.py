# Generated by Django 4.0.2 on 2022-03-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0005_alter_empleado_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]