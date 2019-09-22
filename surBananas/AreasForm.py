from django import forms
from .models import areas
class AreasForm(forms.ModelForm):
    class Meta:
        model = areas
        fields = ['fase', 'puesto', 'actividad', 'tiposRiesgo', 'regionAnatomica', 'eppUtilizar']

        labels = {'class': 'bmd-label-floating',
                  'fase': '',
                  'puesto': '',
                  'actividad': '',
                  'tiposRiesgo': '',
                  'eppUtilizar': '',
                  'empleado': '',
                  }
        widgets = {
            'fase': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fase',

                }
            ),
            'puesto': forms.Select(
                attrs={
                    'class': 'form-control',

                }
            ),
            'actividad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Actividad',

                }
            ),
            'tiposRiesgo': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'regionAnatomica': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Región Anatomica',

                }
            ),
            'eppUtilizar': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'EPP a Utilizar',

                }
            ),


        }