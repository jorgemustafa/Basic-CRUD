from datetime import date, timedelta
from urllib import request

from django.conf import settings
from django.core.management.base import BaseCommand
from apps.acordos_ae.models import AcordoAereo
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Command(BaseCommand):
    help = 'Enviar email - Aviso vencimento de contrato'

    def handle(self, *args, **options):
        data_venc = date.today() + timedelta(days=30)
        acordos = AcordoAereo.objects.filter(ativo=True)

        for acordo in acordos:
            if data_venc >= acordo.validade:

                html_content = render_to_string("email_template.html",{'acordo':acordo})
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    #Assunto
                    'O Vencimento do Acordo {} Está Próximo'.format(acordo.acordo),

                    #Conteúdo HTML -> email_template.html
                    text_content,

                    #Remetente
                    settings.EMAIL_HOST_USER,

                    #Destinatário
                    [acordo.cliente.executivo.email],
                )

                email.attach_alternative(html_content, 'text/html')
                email.send()