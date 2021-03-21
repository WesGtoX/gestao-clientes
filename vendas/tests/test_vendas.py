from django.test import TestCase

from produtos.models import Produto
from vendas.models import Venda, ItemDoPedido


class VendasTestCase(TestCase):

    def setUp(self) -> None:
        self.venda = Venda.objects.create(numero='123', desconto=10, status='AB')
        self.produto = Produto.objects.create(descricao='Produto 1', preco=10)

    def test_verifica_num_vendas(self):
        self.assertEqual(Venda.objects.all().count(), 1)

    def test_valor_venda(self):
        """
        Verifica valor total da venda
        """
        ItemDoPedido.objects.create(venda=self.venda, produto=self.produto, quantidade=10, desconto=10)
        self.assertEqual(self.venda.valor, 80)

    def test_desconto(self):
        self.assertEqual(self.venda.desconto, 10)

    def test_item_incluido_na_lista_items(self):
        item = ItemDoPedido.objects.create(venda=self.venda, produto=self.produto, quantidade=1, desconto=0)
        self.assertIn(item, self.venda.itemdopedido_set.all())

    def test_checa_nfe_nao_emitida(self):
        self.assertFalse(self.venda.nfe_emitida)

    def test_checa_status(self):
        self.venda.status = 'PC'
        self.venda.save()
        self.assertEqual(self.venda.status, 'PC')
