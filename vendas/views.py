from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
# from django.db.models import Min, Max, Avg, Count

from vendas.models import Venda, ItemDoPedido
from vendas.forms import ItemPedidoForm, ItemDoPedidoModelForm


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
        count_vendas = vendas.count()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas, 'count_vendas': count_vendas})


class NovoPedidoView(View):

    def get(self, request):
        data = {'itens': ItemDoPedido.objects.all()}
        return render(request, 'vendas/novo-pedido.html', data)

    def post(self, request):
        data = {
            'form_item': ItemPedidoForm(),
            'numero': request.POST.get('numero'),
            'desconto': request.POST.get('desconto').replace(',', '.'),
            'venda_id': request.POST.get('venda_id')
        }

        if data.get('venda_id'):
            venda = Venda.objects.get(id=data.get('venda_id'))
            venda.desconto = data.get('desconto')
            venda.numero = data.get('numero')
            venda.save()
        else:
            venda = Venda.objects.create(numero=data.get('numero'), desconto=data.get('desconto'))

        itens = venda.itemdopedido_set.all()
        data['venda'] = venda
        data['itens'] = itens

        return render(request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):

    def get(self, request, pk):
        ...

    def post(self, request, venda):

        item, item_exists = ItemDoPedido.objects.get_or_create(
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
            'venda': item.venda,
            'itens': item.venda.itemdopedido_set.all()
        }

        if item_exists:
            data['mensagem'] = 'Item já incluido no peiddo, por favor edite o item.'

        return render(request, 'vendas/novo-pedido.html', data)


class EditPedidoView(View):

    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)

        data = {
            'form_item': ItemPedidoForm(),
            'numero': venda.numero,
            'desconto': venda.desconto,
            'venda': venda,
            'itens': venda.itemdopedido_set.all()
        }

        return render(request, 'vendas/novo-pedido.html', data)


class EditItemPedidoView(View):

    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        form = ItemDoPedidoModelForm(instance=item_pedido)
        return render(request, 'vendas/edit-itempedido.html', {'item_pedido': item_pedido, 'form': form})

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)

        item_pedido.quantidade = request.POST.get('quantidade')
        item_pedido.desconto = request.POST.get('desconto')
        item_pedido.save()

        venda_id = item_pedido.venda.id
        return redirect('edit-pedido', venda=venda_id)


class DeletePedidoView(View):

    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(request, 'vendas/delete-pedido-confirm.html', {'venda': venda})

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('lista-vendas')


class DeleteItemPedidoView(View):

    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        return render(request, 'vendas/delete-itempedido-confirm.html', {'item_pedido': item_pedido})

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()
        return redirect('edit-pedido', venda=venda_id)
