from django import forms
from .models import empleados
class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ['fase','codigoEmpleado','nombres', 'apellidoPaterno', 'apellidoMaterno', 'edad', 'fechaNacimiento','fechaEliminacion','motivoEliminacion', 'numeroSeguroSocial','curp', 'rfc', 'estadoCivil',
                  'nacionalidad', 'area', 'telefono', 'celular', 'correoElectronico', 'direccion', 'ciudad', 'colonia', 'codigoPostal', 'estado', 'imagen', 'status']

        labels = {'class': 'bmd-label-floating',
                  'fase':'',
                  'codigoEmpleado': '',
                  'nombres': '',
                  'apellidoPaterno': '',
                  'apellidoMaterno': '',
                  'edad': '',
                  'fechaNacimiento': '',
                  'fechaEliminacion': '',
                  'motivoEliminacion': '',
                  'numeroSeguroSocial': '',
                  'curp': '',
                  'rfc': '',
                  'estadoCivil': '',
                  'nacionalidad': '',
                  'area': '',
                  'telefono': '',
                  'celular': '',
                  'correoElectronico':'',
                  'direccion':'',
                  'ciudad': '',
                  'colonia': '',
                  'codigoPostal': '',
                  'estado': '',
                  'imagen': '',
                  'status': ''
                  }

        widgets = {
            'fase': forms.Select(
                attrs={
                    'class':'form-control',
                    
                }
            ),

            'codigoEmpleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo de empleado',

                }
            ),
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
            'fechaEliminacion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha de Eliminación',

                }
            ),
             'motivoEliminacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Motivos de Eliminacion',

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
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nacionalidad',

                }
            ),
            'area': forms.Select(
                attrs={
                    'class': 'form-control'

                }
            ),
            # 'labor': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Labor',
            #
            #     }
            # ),
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

             'status': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado',

                }
            ),


        }
