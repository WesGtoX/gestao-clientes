# Generated by Django 2.2.6 on 2021-01-07 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20210107_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='ItemsDoPedido',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Venda',
        ),
    ]
