from django.urls import path
from vendas import views


urlpatterns = [
    path('list/', views.vendas_list, name='vendas_list'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
