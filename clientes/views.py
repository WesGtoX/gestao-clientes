from django.urls import reverse_lazy
from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.views.generic import View, list, detail, edit

from clientes.models import Person, Produto, Venda
from clientes.forms import PersonForm


@login_required
def persons_list(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'person.html', context)


@login_required
def persons_new(request):
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
class PersonList(list.ListView):

    model = Person  # lista de uma forma mais simples e limpa


# DetailView
class PersonDetail(detail.DetailView):

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
class PersonDelete(edit.DeleteView):

    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


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
