# Generated by Django 3.0.4 on 2022-04-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_detalle_stock', '0005_auto_20220308_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_stock',
            name='piscinas',
            field=models.CharField(blank=True, default='Todas las Piscinas', max_length=250, null=True),
        ),
    ]