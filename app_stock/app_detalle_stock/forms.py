from tkinter.tix import Select

from django.forms import *
from app_stock.app_detalle_stock.models import Producto_Stock, Total_Stock, InvoiceStock

OPCIONES_ESCOGER = (
    ('INGRESO', 'INGRESO'),
    ('EGRESO', 'EGRESO'),
)


class ProdStockForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ProdStockForm, self).__init__(*args, **kwargs)
    #     self.fields['producto_empresa'].queryset = Total_Stock.objects.filter(nombre_empresa__siglas='PSM')

    class Meta:
        model = Producto_Stock
        fields = '__all__'
        widgets = {
            'producto_empresa': Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly': 'readonly'
                }
            ),
            'cantidad_ingreso': NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly': 'readonly'
                }
            ),
            'cantidad_usar': NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'cantidad_egreso': NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly': 'readonly'
                }
            ),
            'tipo': Select(choices=OPCIONES_ESCOGER,
                           attrs={
                               'class': 'form-control'
                           }
                           ),
            'fecha_ingreso': DateInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'required': True
                },
                format='%Y-%m-%d'
            ),
            'numero_guia': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un número de guia',
                    'required': True
                }
            ),
            'responsable_ingreso': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un responsable',
                    'required': True
                }
            )

        }

        exclude = ['piscinas']


class InvoiceStockForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ProdStockForm, self).__init__(*args, **kwargs)
    #     self.fields['producto_empresa'].queryset = Total_Stock.objects.filter(nombre_empresa__siglas='PSM')

    class Meta:
        model = InvoiceStock
        fields = '__all__'
        widgets = {
            'fecha_ingreso': DateInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'required': True
                },
                format='%Y-%m-%d'
            ),
            'numero_guia': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un número de guia',
                    'required': True
                }
            ),
            'responsable_ingreso': TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'placeholder': 'Ingrese un responsable',
                    'required': True
                }
            )

        }

        exclude = ['piscinas']


class ProdStockTotalForm(ModelForm):
    class Meta:
        model = Total_Stock
        fields = '__all__'
        widgets = {
            'nombre_prod': Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'nombre_empresa': Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'stock': NumberInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            )

        }
