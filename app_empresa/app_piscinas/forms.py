
from django.forms import *

from app_empresa.app_reg_empresa.models import Piscinas


class PiscinasForm(ModelForm):
    class Meta:
        model = Piscinas
        fields = '__all__'
        widgets = {
            'orden': NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número de piscina',
                    'autocomplete':'off'
                }
            ),
            'numero': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Piscina ejemplo Piscina 1',
                    'autocomplete': 'off'
                }
            ),
            'empresa': Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'hect': TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese las Hectáreas de Piscina',
                    'autocomplete':'off'
                }
            )

        }