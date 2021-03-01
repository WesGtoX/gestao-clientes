from django.urls import path
from vendas import views


urlpatterns = [
    path('', views.ListaVendasView.as_view(), name='lista-vendas'),
    path('novo-pedido/', views.NovoPedidoView.as_view(), name='novo-pedido'),
    path('novo-item-pedido/<int:venda>', views.NovoItemPedido.as_view(), name='novo-item-pedido'),
    path('list/', views.vendas_list, name='vendas_list'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
