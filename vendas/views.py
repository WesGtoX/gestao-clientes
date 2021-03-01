from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
# from django.db.models import Min, Max, Avg, Count

from vendas.models import Venda, ItemDoPedido
from vendas.forms import ItemPedidoForm


@login_required
def vendas_list(request):
    vendas = Venda.objects.all()
    context = {'vendas': vendas}
    return render(request, 'venda.html', context)


class DashboardView(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.show_dashboard'):
            return HttpResponse('Acesso negado, você precisa de permissão!')

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {}

        context['media'] = Venda.objects.media()
        context['media_dec'] = Venda.objects.media_dec()
        context['min'] = Venda.objects.min()
        context['max'] = Venda.objects.max()
        context['num_ped'] = Venda.objects.num_ped()
        context['num_ped_nfe'] = Venda.objects.num_ped_nfe()

        # context['media'] = Venda.objects.all().aggregate(Avg('valor')).get('valor__avg')
        # context['media_dec'] = Venda.objects.all().aggregate(Avg('desconto')).get('desconto__avg')
        # context['min'] = Venda.objects.all().aggregate(Min('valor')).get('valor__min')
        # context['max'] = Venda.objects.all().aggregate(Max('valor')).get('valor__max')
        # context['num_ped'] = Venda.objects.all().count()
        # context['num_ped_nfe'] = Venda.objects.filter(nfe_emitida=True).aggregate(Count('id')).get('id__count')

        return render(request, 'vendas/dashboard.html', context)


class ListaVendasView(View):

    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})


class NovoPedidoView(View):

    def get(self, request):
        data = {'itens': ItemDoPedido.objects.all()}
        return render(request, 'vendas/novo-pedido.html', data)

    def post(self, request):
        data = {
            'form_item': ItemPedidoForm(),
            'numero': request.POST.get('numero'),
            'desconto': request.POST.get('numero'),
            'venda': request.POST.get('venda_id')
        }

        if data.get('venda'):
            venda = Venda.objects.get(id=data.get('venda'))
            venda.desconto = data.get('desconto')
            venda.numero = data.get('numero')
            venda.save()
        else:
            venda = Venda.objects.create(numero=data.get('numero'), desconto=data.get('desconto'))

        itens = venda.itemdopedido_set.all()
        data['venda_obj'] = venda
        data['itens'] = itens

        return render(request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):

    def get(self, request, pk):
        ...

    def post(self, request, venda):
        item = ItemDoPedido.objects.create(
            produto_id=request.POST.get('produto_id'),
            quantidade=request.POST.get('quantidade'),
            desconto=request.POST.get('desconto'),
            venda_id=venda
        )

        data = {
            'item': item,
            'form_item': ItemPedidoForm(),
            'numero': item.venda.numero,
            'desconto': item.venda.desconto,
            'venda': item.venda.id,
            'venda_obj': item.venda,
            'itens': item.venda.itemdopedido_set.all()
        }

        return render(request, 'vendas/novo-pedido.html', data)
