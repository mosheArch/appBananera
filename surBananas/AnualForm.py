from django import forms
from .models import planAnual
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
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
                'objetivoG': SummernoteWidget(
                 attrs={
                    
                 }
                ),


            'dirigido':SummernoteWidget(
                 attrs={
                     
                 }
                ),
            'tema':SummernoteWidget(),
            # 'tema': forms.Textarea(
            #     attrs={
            #     'foo': SummernoteWidget(),
	        #     'bar': SummernoteInplaceWidget(),
            #     'class':'form-control',
            #     'placeholder':'TEMA(S)',
            #     'rows':'3',

            #     }
            # ),
            'objetivoe': SummernoteWidget(),
            'contenido':SummernoteWidget(
                attrs={
                # 'class':'form-control',
                # 'placeholder':'CONTENIDO',
                #  'rows':'3',

                }
            ),
            'tecnicas': SummernoteWidget(),


            'dirigidoaquien':SummernoteWidget(
                attrs={
                # 'class':'form-control',
                # 'placeholder':'A QUIEN VA DIRIGIDO',
                #  'rows':'3',
                }
            ),
            'duracion':SummernoteWidget(
                attrs={
                # 'class': 'form-control',
                # 'placeholder':'DURACION',
                #  'rows':'3',
                }
            ),

          


        }