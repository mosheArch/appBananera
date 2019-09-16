from django import forms
from .models import programasCapacitacion

class ProgramasCapacitacion(forms.ModelForm):
    class Meta:
        model = programasCapacitacion

        fields = ['temaCapacitacion', 'descripcionCapacitacion', 'tipoCapacitacion']

        labels = {'class': 'bmd-label-floating',
                  'temaCapactacion': '',
                  'descripcionCapacitacion': '',
                  'tipoCapacitacion': ''}

        widgets = {
            'temaCapacitacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Tema',

                }
            ),
            'descripcionCapacitacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del Tema',

                }
            ),
            'tipoCapacitacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tipo de Tema',

                }
            ),
        }
