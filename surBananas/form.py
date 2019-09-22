from django import forms
from .models import empleados
class EmpleadosForm(forms.ModelForm):
    class Meta:
        model =  empleados
        fields = ['nombres', 'apellidoPaterno', 'apellidoMaterno', 'edad', 'fechaNacimiento', 'numeroSeguroSocial','curp', 'rfc', 'estadoCivil',
                  'nacionalidad', 'area', 'labor', 'telefono', 'celular', 'correoElectronico', 'direccion', 'ciudad', 'colonia', 'codigoPostal', 'estado', 'imagen']

        labels = {'class': 'bmd-label-floating',
                  'nombres':'',
                  'apellidoPaterno':'',
                  'apellidoMaterno': '',
                  'edad': '',
                  'fechaNacimiento': '',
                  'numeroSeguroSocial': '',
                  'curp': '',
                  'rfc': '',
                  'estadoCivil': '',
                  'nacionalidad': '',
                  'area': '',
                  'labor': '',
                  'telefono': '',
                  'celular': '',
                  'correoElectronico':'',
                  'direccion':'',
                  'ciudad': '',
                  'colonia': '',
                  'codigoPostal':'',
                  'estado':'',
                  'imagen': ''
                  }

        widgets = {
            'nombres': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombres',

                }
            ),

            'apellidoPaterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Paterno',

                }
            ),
            'apellidoMaterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Materno',

                }
            ),
            'edad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',

                }
            ),
            'fechaNacimiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha de Nacimiento',

                }
            ),
            'numeroSeguroSocial': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seguro Social',

                }
            ),
            'curp': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'CURP',

                }
            ),
            'rfc': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'RFC',

                }
            ),
            'estadoCivil': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado Civil',

                }
            ),
            'nacionalidad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'area': forms.Select(
                attrs={
                    'class': 'form-control'

                }
            ),
            'labor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Labor',

                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',

                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Celular',

                }
            ),
            'correoElectronico': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',

                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'type':'file',
                    'class': 'file-upload',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Direccion',

                }
            ),
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ciudad',

                }
            ),
            'colonia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Colonia',

                }
            ),
            'codigoPostal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo Postal',

                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado',

                }
            ),


        }
