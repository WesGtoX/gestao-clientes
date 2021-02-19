from django.urls import path
from django.views.generic.base import TemplateView
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.my_logout, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html')),  # Introdução e TemplateViews
    path('home3/', views.HomePageView.as_view(template_name='home3.html')),  # Introdução e TemplateViews
    path('view/', views.MyView.as_view()),  # View, a mais simples e básica de todas
    path('polices/', views.polices, name='polices'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
]
