from django.db.models import Manager, Min, Max, Avg, Count


class VendaManager(Manager):

    def media(self):
        return self.all().aggregate(Avg('valor')).get('valor__avg')

    def media_dec(self):
        return self.all().aggregate(Avg('desconto')).get('desconto__avg')

    def min(self):
        return self.all().aggregate(Min('valor')).get('valor__min')

    def max(self):
        return self.all().aggregate(Max('valor')).get('valor__max')

    def num_ped(self):
        return self.all().count()

    def num_ped_nfe(self):
        return self.filter(nfe_emitida=True).aggregate(Count('id')).get('id__count')
