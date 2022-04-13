
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from Sistema_Camaronera.settings import MEDIA_URL, STATIC_URL
# Create your models here.


class Empresa(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre Empresa ', unique=True)
    ruc = models.CharField(max_length=13, unique=True, verbose_name='RUC ')
    direccion = models.CharField(max_length=150, verbose_name='Direccion ')
    siglas = models.CharField(max_length=150, verbose_name='Siglas ', unique=True)
    aperturada = models.DateField(default=datetime.now, verbose_name='Fecha de Apertura ', null=True, blank=True)
    actividad = models.CharField(max_length=150, verbose_name='Actividad ')
    estado = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='logo_comp/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.nombre

    def get_image(self):
        if self.logo:
            return '{}{}'.format(MEDIA_URL, self.logo)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['logo'] = self.get_image()
        item['aperturada'] = self.aperturada.strftime('%Y-%m-%d')
        return item


    class Meta:
        db_table = 'tb_empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id']


class Piscinas(models.Model):
    orden = models.IntegerField(default=0, verbose_name='Orden de las Piscinas ')
    numero = models.CharField(max_length=150, unique=True, verbose_name='Número de Piscina ')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa ")
    hect = models.CharField(max_length=150, verbose_name='Hectáreas de Dimensiones')
    pis = models.BooleanField(default=True, verbose_name="Piscina ")
    prec = models.BooleanField(default=True, verbose_name="Precria ")
    estado = models.BooleanField(default=True, verbose_name="Estado ")

    def __str__(self):
        return self.numero
    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     try:
    #         nueva_piscina = super(Piscinas, self).save()
    #
    #         if self.orden:
    #             self.numero = 'PISCINA %s' % self.orden
    #     except Exception as exc:
    #         pass
    def toJSON(self):
        item = model_to_dict(self)
        item['empresa'] = self.empresa.toJSON()
        return item

    class Meta:
        db_table = 'tb_piscina'
        verbose_name = 'Piscina'
        verbose_name_plural = 'Piscinas'
        ordering = ['id']