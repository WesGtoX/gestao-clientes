from django.urls import path
from vendas import views


urlpatterns = [
    path('', views.ListaVendasView.as_view(), name='lista-vendas'),

    path('novo-pedido/', views.NovoPedidoView.as_view(), name='novo-pedido'),
    path('edit-pedido/<int:venda>', views.EditPedidoView.as_view(), name='edit-pedido'),
    path('delete-pedido/<int:venda>', views.DeletePedidoView.as_view(), name='delete-pedido'),

    path('novo-item-pedido/<int:venda>', views.NovoItemPedido.as_view(), name='novo-item-pedido'),
    path('edit-item-pedido/<int:item>', views.EditItemPedidoView.as_view(), name='edit-item-pedido'),
    path('delete-item-pedido/<int:item>', views.DeleteItemPedidoView.as_view(), name='delete-item-pedido'),

    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('list/', views.vendas_list, name='vendas_list'),
]
