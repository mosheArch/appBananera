from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from .models import empleados
from django.views.generic import ListView, DetailView

class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = empleados
    template_name = 'card.html'
""" 
class HelloPDFView(PDFTemplateView):
    capacitar = empleados
    context_object_name = 'card'
    template_name = 'card.html'
    queryset = empleados.objects.filter(status=True) """

class HelloPDFView(PDFTemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            **kwargs
        )