from django.contrib import admin
from clientes.models import Person, Documento, Venda, Produto
from clientes.actions import nfe_emitida, nfe_nao_emitida


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


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):

    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa', 'produtos')
    raw_id_fields = ('pessoa',)
    list_display = ('numero', 'valor', 'pessoa', 'nfe_emitida', 'get_total', 'get_total_from_admin')
    list_filter = ('pessoa', 'pessoa__doc', 'valor')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    # filter_vertical = ['produtos']
    # filter_horizontal = ['produtos']

    def get_total_from_admin(self, obj):
        return obj.get_total()

    get_total_from_admin.short_description = 'Total do Admin'


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ('id', 'preco', 'descricao')
    search_fields = ['id', 'descricao']


# admin.site.register(PersonAdmin)
# admin.site.register(Documento)
# admin.site.register(Venda)
# admin.site.register(Produto)
