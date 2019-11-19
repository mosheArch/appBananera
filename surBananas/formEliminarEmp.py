from django import forms
from .models import empleados
class EmpleadosFormEliminar(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ['fechaEliminacion','motivoEliminacion', 'status']

        labels = {'class': 'bmd-label-floating',
                  
                  'fechaEliminacion': '',
                  'motivoEliminacion': '',
                  
                  'status': ''
                  }

        widgets = {
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
            'status': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado',

                }
            ),


        }
