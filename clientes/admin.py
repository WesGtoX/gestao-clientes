from django.contrib import admin
from clientes.models import Person, Documento, TabelaExistente


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Dados Pessoais', {'fields': ('first_name', 'last_name', 'age', 'doc')}),
        ('Dados Complementares', {
            'classes': ('collapse',),
            'fields': ('salary', 'bio', 'photo')
        })
    )
    # fields = ('first_name', 'last_name', ('age', 'doc'), 'salary', 'bio', 'photo')
    # exclude = ('bio',)
    autocomplete_fields = ('doc',)
    list_display = ('first_name', 'last_name', 'age', 'salary', 'have_photo')
    list_filter = ('age', 'salary')
    search_fields = ('id', 'first_name')

    def have_photo(self, obj):
        if not obj.photo:
            return 'Não'
        return 'Sim'

    have_photo.short_description = 'Possui Foto'


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):

    list_display = ('num_doc',)
    search_fields = ['id', 'num_doc']


@admin.register(TabelaExistente)
class TabelaExistenteAdmin(admin.ModelAdmin):

    list_display = ('nome', 'salario')
    search_fields = ['nome', 'salario']
