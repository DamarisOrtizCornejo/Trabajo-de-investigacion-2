# Generated by Django 4.0.2 on 2022-03-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnomina', '0002_alter_cargo_options_alter_departamento_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['id'], 'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterField(
            model_name='cargo',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]