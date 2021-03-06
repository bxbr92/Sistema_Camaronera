# Generated by Django 3.0.4 on 2022-02-22 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=400, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'tb_categoria',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('gramaje', models.CharField(blank=True, max_length=100, null=True, verbose_name='Gramaje')),
                ('descripcion', models.CharField(blank=True, max_length=400, null=True, verbose_name='Sub-Categoria ')),
                ('presentacion', models.CharField(blank=True, max_length=400, null=True, verbose_name='Presentacion ')),
                ('peso_presentacion', models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True, verbose_name='Peso de la Presentacion ')),
                ('unid_medida', models.CharField(blank=True, max_length=400, null=True, verbose_name='Unidad de Medida de la Presentación ')),
                ('unid_aplicacion', models.CharField(blank=True, max_length=400, null=True, verbose_name='Aplicación en ')),
                ('minimo_stock', models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True, verbose_name='Stock Mínimo ')),
                ('costo', models.DecimalField(decimal_places=10, default=0.0, max_digits=19)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('aplic_directa', models.BooleanField(default=False, verbose_name='Aplicación Directa ')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Seleccionar Imagen ')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_categoria.Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'tb_producto',
                'ordering': ['id'],
            },
        ),
    ]
