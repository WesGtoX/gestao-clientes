# Generated by Django 2.2.6 on 2021-01-07 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemsDoPedido',
            new_name='ItemDoPedido',
        ),
    ]
