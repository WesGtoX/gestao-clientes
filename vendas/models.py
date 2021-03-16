from django.db import models
from django.db.models import F, FloatField, Sum

# from django.db.models.signals import m2m_changed
from django.db.models.signals import post_save
from django.dispatch import receiver

from clientes.models import Person
from produtos.models import Produto
from vendas.managers import VendaManager


class Venda(models.Model):

    ABERTA = 'AB'
    FECHADA = 'FC'
    PROCESSANDO = 'PC'
    DESCONHECIDO = 'DC'

    STATUS = (
        (ABERTA, 'Aberta'),
        (FECHADA, 'Fechada'),
        (PROCESSANDO, 'Processando'),
        (DESCONHECIDO, 'Desconhecido')
    )

    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS, default=DESCONHECIDO, max_length=2)

    objects = VendaManager()

    class Meta:
        permissions = (
            ('setar_nfe', 'Usuário pode alterar parametro NF-e'),
            ('show_dashboard', 'Pode visualizar o dashboard'),
            ('permissao3', 'Permissão 3')
        )

    def get_total(self):
        total = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco') - F('desconto')), output_field=FloatField())
        )['tot_ped'] or 0

        total = total - float(self.impostos) - float(self.desconto)
        self.valor = total
        Venda.objects.filter(id=self.id).update(valor=total)

    # def get_total(self):
    #     total = 0
    #     for produto in self.produtos.all():
    #         total += produto.preco
    #
    #     return (total - self.desconto) - self.impostos

    def __str__(self):
        return self.numero


class ItemDoPedido(models.Model):

    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField(default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.venda.numero} - {self.produto.descricao}'

    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
        unique_together = (
            ('venda', 'produto'),
        )


@receiver(post_save, sender=ItemDoPedido)
def update_vendas_total_item(sender, instance, **kwargs):
    instance.venda.get_total()


@receiver(post_save, sender=Venda)
def update_vendas_total_venda(sender, instance, **kwargs):
    instance.get_total()


# @receiver(m2m_changed, sender=Venda.produtos.through)
# def update_vendas_total(sender, instance, **kwargs):
#     instance.valor = instance.get_total()
#     instance.save()
#     # Venda.objects.filter(id=instance.id).update(total=total)
