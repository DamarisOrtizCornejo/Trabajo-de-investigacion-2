# Generated by Django 4.0.2 on 2022-03-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0007_alter_departamento_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cedula',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]
