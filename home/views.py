from django.http import HttpResponse

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout

from django.views import View
from django.views.generic.base import TemplateView


# TODO: Refact to use threads soon as possible
def home(request):
    template_name = 'home/home.html'
    # import pdb; pdb.set_trace()  # TODO: modo hard de debugar
    # value1, value2 = 10, 20
    # c = value1 * value2
    # context = {}
    # context['result'] = c
    return render(request, template_name)  # , context)


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
        context['minha_variavel'] = 'Ola, seja bem vindo ao curso de Django avancado'
        return context


# View, a mais simples e básica de todas
class MyView(View):

    def get(self, request, *args, **kwargs):
        response = render_to_response('home3.html')
        response.set_cookie('color', 'blue', max_age=1000)
        return response
        # return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')


def polices(request):
    return render(request, 'polices.html')


def terms_of_use(request):
    return render(request, 'terms-of-use.html')
