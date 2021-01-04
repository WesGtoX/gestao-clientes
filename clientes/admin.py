from django.contrib import admin
from clientes.models import Person, Documento, Venda, Produto


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
    list_display = ('first_name', 'last_name', 'age', 'salary', 'have_photo')
    list_filter = ('age', 'salary')

    def have_photo(self, obj):
        if not obj.photo:
            return 'Não'
        return 'Sim'

    have_photo.short_description = 'Possui Foto'


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):

    readonly_fields = ('valor',)
    raw_id_fields = ('pessoa',)
    list_display = ('numero', 'valor', 'pessoa', 'get_total', 'get_total_from_admin')
    list_filter = ('pessoa', 'pessoa__doc', 'valor')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')

    def get_total_from_admin(self, obj):
        return obj.get_total()

    get_total_from_admin.short_description = 'Total do Admin'


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ('id', 'preco', 'descricao')


# admin.site.register(PersonAdmin)
admin.site.register(Documento)
# admin.site.register(Venda)
# admin.site.register(Produto)
