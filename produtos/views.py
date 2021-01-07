from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.generic import View

from produtos.models import Produto


@login_required
def produtos_list(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produto.html', context)


# Bulk create
class ProdutoBulk(View):

    def get(self, request):
        produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)
        return HttpResponse('Funcionou')
