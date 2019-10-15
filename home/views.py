from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


# TODO: Refact to use threads soon as possible
def home(request):
    # import pdb; pdb.set_trace()   # TODO: modo hard de debugar
    value1 = 10
    value2 = 20
    c = value1 * value2
    return render(request, 'home.html', {'result': c})


# FIXME: Fix bug...
def my_logout(request):
    logout(request)
    return redirect('home')


# CLASS BASED VIEWS
# Introdução e TemplateViews
class HomePageView(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = "Ola, seja bem vindo ao curso de Django avancado"
        return context

# View, a mais simples e básica de todas
class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')