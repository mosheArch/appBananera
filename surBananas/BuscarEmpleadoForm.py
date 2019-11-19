from django import forms
from .models import incidencias
class IncidenciasForm(forms.ModelForm):
    class Meta:
        model = incidencias
        fields = ['totalfaltas','codigoEmpleado']

        labels = {'class': 'bmd-label-floating',
                  'codigoEmpleado':'',
                  'totalfaltas:':'',
                 

                  }
        widgets = {
            'codigoEmpleado': forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
              'totalfaltas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': 1,
                    'hidden':'True',

                }
            ),


    

       
        }
