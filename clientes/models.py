from django.conf import settings
from django.db import models

from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string


class Documento(models.Model):

    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def nome_completo(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        data = {'cliente': self.first_name}
        plain_text = render_to_string('clientes/emails/novo_cliente.txt', data)
        html_email = render_to_string('clientes/emails/novo_cliente.html', data)

        send_mail(
            subject='Novo cliente cadastrado',
            message=plain_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            html_message=html_email,
            fail_silently=False
        )

        mail_admins(
            subject='Novo cliente cadastrado',
            message=plain_text,
            html_message=html_email,
            fail_silently=False
        )

        # message1 = (
        #     'Subject here',
        #     'Here is the message',
        #     settings.EMAIL_HOST_USER,
        #     ['first@gestaoclientes.com.br', 'other@gestaoclientes.com.br']
        # )
        # message2 = (
        #     'Another Subject',
        #     'Here is another message',
        #     settings.EMAIL_HOST_USER,
        #     ['second@gestaoclientes.com.br']
        # )
        # send_mass_mail((message1, message2), fail_silently=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar clientes'),
        )
