from django import forms
from .models import capacitacion
class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = capacitacion
        fields = ['empleado', 'programas', 'fechaCapacitacion']

        labels = {'class': 'bmd-label-floating',
                  'empleado': '',
                  'programas': '',
                  'fechaCapacitacion': '',

                  }
        widgets = {
            'empleado': forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            'programas': forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            'fechaCapacitacion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',

                }
            ),


        }