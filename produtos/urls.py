from django.urls import path
from produtos import views


urlpatterns = [
    path('list/', views.produtos_list, name='produtos_list'),
    path('produto_bulk/', views.ProdutoBulk.as_view(), name='produto_bulk'),  # CreateView
]
