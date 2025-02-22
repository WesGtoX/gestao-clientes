# Generated by Django 2.2.6 on 2021-02-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20210119_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuário pode alterar parametro NF-e'), ('permissao2', 'Permissão 2'), ('permissao3', 'Permissão 3'))},
        ),
        migrations.AlterField(
            model_name='itemdopedido',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='itemdopedido',
            name='quantidade',
            field=models.FloatField(default=0),
        ),
    ]
