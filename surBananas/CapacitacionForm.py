from django import forms
from .models import capacitacion
class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = capacitacion
        fields = ['nombreCapacitacion','empleado', 'programas', 'fechaCapacitacion']

        labels = {'class': 'bmd-label-floating',
                  'nombreCapacitacion':'',
                  'empleado': '',
                  'programas': '',
                  'fechaCapacitacion': '',

                  }
        widgets = {
            'nombreCapacitacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Capacitacion',

                }
            ),
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