# Generated by Django 3.0.4 on 2022-02-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='gramaje',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Gramaje '),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre '),
        ),
    ]
