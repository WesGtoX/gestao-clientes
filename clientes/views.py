from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.views.generic import list, detail, edit

from clientes.models import Person
from produtos.models import Produto
from vendas.models import Venda
from clientes.forms import PersonForm


@login_required
def persons_list(request):
    query = Q(first_name__icontains=request.GET.get('pesquisa', ''))
    query.add(Q(last_name__icontains=request.GET.get('pesquisa', '')), Q.OR)
    persons = Person.objects.filter(query)

    context = {'persons': persons}
    return render(request, 'person.html', context)


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Não autorizado')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    context = {'form': form}
    return render(request, 'person_form.html', context)


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    context = {'form': form}
    return render(request, 'person_form.html', context)


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    context = {'person': person}
    return render(request, 'person_delete_confirm.html', context)


# CLASS BASED VIEW
# ListView
class PersonList(LoginRequiredMixin, list.ListView):

    model = Person  # lista de uma forma mais simples e limpa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_access = self.request.session.get('fist_access', False)

        if not first_access:
            context['message'] = 'Sejá bem vindo ao seu primeiro acesso hoje!'
            self.request.session['fist_access'] = True
        else:
            context['message'] = 'Você já acessou hoje!'

        return context


# DetailView
class PersonDetail(LoginRequiredMixin, detail.DetailView):

    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(pessoa_id=self.object.id)
        return context


# CreateView
class PersonCreate(edit.CreateView):

    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


# UpdateView
class PersonUpdate(edit.UpdateView):

    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


# DeleteView
class PersonDelete(PermissionRequiredMixin, edit.DeleteView):

    model = Person
    permission_required = ('clientes.deletar_clientes',)
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


def api(request):
    # data = {'nome': 'Wesley', 'idade': 26, 'salario': 150000}
    # mensagem = {'mensagem': 'xyz'}
    # return JsonResponse(mensagem, status=404)
    # return JsonResponse(data, status=200)

    # produto = Produto.objects.last()
    # data = {'descricao': produto.descricao, 'preco': produto.preco}
    # data = model_to_dict(produto)

    data = []

    produtos = Produto.objects.all()

    for produto in produtos:
        data.append(model_to_dict(produto))

    return JsonResponse(data, status=200, safe=False)


class APICBV(View):

    def get(self, request):
        # data = {'nome': 'Wesley'}

        # produto = Produto.objects.last()
        # data = model_to_dict(produto)

        data = []

        produtos = Produto.objects.all()

        for produto in produtos:
            data.append(model_to_dict(produto))

        return JsonResponse(data)

    def post(self):
        # Forbiden csrf_token
        pass
