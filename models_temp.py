# ./manage.py inspectdb > models_temp.py
#
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Minhatabela(models.Model):
    nome = models.TextField()
    salario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'MinhaTabela'


class Tabela1(models.Model):
    nome = models.TextField()
    salario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Tabela1'


class Tabela2(models.Model):
    nome = models.TextField()
    salario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Tabela2'


class Tabela3(models.Model):
    nome = models.TextField()
    salario = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Tabela3'


class AccountEmailaddress(models.Model):
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
# Unable to inspect table 'auth_group_permissions'
# The error was: list index out of range


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
# Unable to inspect table 'auth_user_groups'
# The error was: list index out of range
# Unable to inspect table 'auth_user_user_permissions'
# The error was: list index out of range


class ClientesDocumento(models.Model):
    num_doc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clientes_documento'


class ClientesPerson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    bio = models.TextField()
    photo = models.CharField(max_length=100, blank=True, null=True)
    doc = models.ForeignKey(ClientesDocumento, models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_person'


class DashboardUserdashboardmodule(models.Model):
    title = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    app_label = models.CharField(max_length=255, blank=True, null=True)
    user = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    order = models.IntegerField()
    settings = models.TextField()
    children = models.TextField()
    collapsed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'dashboard_userdashboardmodule'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class JetBookmark(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    user = models.PositiveIntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_bookmark'


class JetPinnedapplication(models.Model):
    app_label = models.CharField(max_length=255)
    user = models.PositiveIntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_pinnedapplication'


class ProdutosProduto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'produtos_produto'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class VendasItemdopedido(models.Model):
    desconto = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    produto = models.ForeignKey(ProdutosProduto, models.DO_NOTHING)
    venda = models.ForeignKey('VendasVenda', models.DO_NOTHING)
    quantidade = models.FloatField()

    class Meta:
        managed = False
        db_table = 'vendas_itemdopedido'


class VendasVenda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    desconto = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    nfe_emitida = models.BooleanField()
    pessoa = models.ForeignKey(ClientesPerson, models.DO_NOTHING, blank=True, null=True)
    impostos = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'vendas_venda'
