from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vendas.models import Venda


@login_required
def vendas_list(request):
    vendas = Venda.objects.all()
    context = {'vendas': vendas}
    return render(request, 'venda.html', context)
