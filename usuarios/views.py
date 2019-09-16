from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from .forms import FormularioLogin
from django.contrib.auth.decorators import login_required


class Login(FormView):
    template_name = 'inicioSesion.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)



    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = super(Login,self).dispatch(request, *args, **kwargs)
            return context

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)

def salirUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')