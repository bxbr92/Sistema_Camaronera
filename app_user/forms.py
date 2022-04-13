
from django.forms import *
from app_user.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña',
                    'autocomplete': 'off'
                }
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña',
                    'autocomplete': 'off'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña',
                    'autocomplete': 'off'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña',
                    'autocomplete': 'off'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña',
                    'autocomplete': 'off'
                }
            ),
            'user_permissions': SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña',
                    'autocomplete': 'off'
                }
            ),

        }

        exclude = ['last_login', 'date_joined', 'groups']