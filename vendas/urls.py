from django.urls import path
from vendas import views


urlpatterns = [
    path('novo-pedido/', views.NovoPedidoView.as_view(), name='novo-pedido'),
    path('list/', views.vendas_list, name='vendas_list'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
