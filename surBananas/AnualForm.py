from django import forms
from .models import planAnual
class Anual(forms.ModelForm):
    class Meta:
        model = planAnual
        fields = ['objetivoG', 'dirigido','tema','objetivoe', 'contenido','tecnicas','dirigidoaquien','duracion']

        labels = {'class': 'bmd-label-floating',
                  'objetivoG': '',
                  'dirigido': '',
                  'tema': '',
                  'objetivoe':'',
                  'contenido':'',
                  'tecnicas':'',
                  'dirigidoaquien':'',
                  'duracion':'',
                  
                
                  }
        widgets = {
            'objetivoG': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'OBJETIVO GENERAL',
                    'rows':'3',

                }
            ),
            'dirigido': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'DIRIGIDO',
                    'rows':'3',

                }
            ),
            'tema': forms.Textarea(
                attrs={
                'class':'form-control',
                'placeholder':'TEMA(S)',
                'rows':'3',

                }
            ),
            'objetivoe': forms.Textarea(
                attrs={
                'class':'form-control',
                'placeholder':'OBJETIVO ESPECIFICO',
                'rows':'3',


                }
            ),
            'contenido': forms.Textarea(
                attrs={
                'class':'form-control',
                'placeholder':'CONTENIDO',
                 'rows':'3',

                }
            ),
            'tecnicas': forms.Textarea(
                attrs={
                'class':'form-control',
                'placeholder':'TECNICAS',
                 'rows':'3',

                }
            ),
            'dirigidoaquien':forms.Textarea(
                attrs={
                'class':'form-control',
                'placeholder':'A QUIEN VA DIRIGIDO',
                 'rows':'3',
                }
            ),
            'duracion':forms.Textarea(
                attrs={
                'class': 'form-control',
                'placeholder':'DURACION',
                 'rows':'3',
                }
            ),

          


        }