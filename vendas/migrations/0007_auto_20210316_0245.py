# Generated by Django 2.2.6 on 2021-03-16 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0006_auto_20210316_0243'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemdopedido',
            unique_together={('venda', 'produto')},
        ),
    ]
