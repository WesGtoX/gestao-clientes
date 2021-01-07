from django.contrib import admin
from vendas.actions import nfe_emitida, nfe_nao_emitida
from vendas.models import Venda, ItemDoPedido


class ItemPedidoInline(admin.TabularInline):

    model = ItemDoPedido
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):

    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa',)
    raw_id_fields = ('pessoa',)
    list_display = ('numero', 'valor', 'pessoa', 'nfe_emitida')
    list_filter = ('pessoa', 'pessoa__doc', 'valor')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemPedidoInline]

    def get_total_from_admin(self, obj):
        return obj.get_total()

    get_total_from_admin.short_description = 'Total do Admin'


@admin.register(ItemDoPedido)
class ItemDoPedidoAdmin(admin.ModelAdmin):

    list_display = ('produto', 'venda', 'quantidade', 'desconto')
