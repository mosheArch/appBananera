from django import forms
from .models import incidencias
class BuscarEmpleadoIncidencias(forms.ModelForm):
    class Meta:
        model = incidencias
        fields = ['codigoEmpleado']

        labels = {'class': 'bmd-label-floating',
                  'codigoEmpleado': ''
                  
                  
                  }
        widgets = {
            'codigoEmpleado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Empleado',

                }
            ),
          
            

        }