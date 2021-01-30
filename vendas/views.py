from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db.models import Min, Max, Avg, Count

from vendas.models import Venda


@login_required
def vendas_list(request):
    vendas = Venda.objects.all()
    context = {'vendas': vendas}
    return render(request, 'venda.html', context)


class Dashboard(View):

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
