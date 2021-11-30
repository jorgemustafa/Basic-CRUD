from datetime import date, timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from apps.acordos_ae.models import AcordoAereo
from apps.colaboradores.models import Colaborador
from apps.clientes.models import Cliente

class Command(BaseCommand):

    help = 'Enviar email - Aviso vencimento de contrato'

    def handle(self, *args, **options):
        data_venc = date.today() + timedelta(days=30)
        acordos = AcordoAereo.objects.filter(ativo=True)
        colaboradores = Colaborador.objects.filter(ativo=True)
        executivos = Cliente.objects.filter(executivo=1)
        print(executivos)

        for acordo in acordos:

            for colaborador in colaboradores:
                email_exec = colaborador.email

                if data_venc >= acordo.validade:
                    send_mail('Vencimento do acordo {} está próximo'.format(acordo.acordo),
                              'O acordo {} do cliente {}, vence em {}, '
                              'favor deixar no radar'.format(
                                  acordo.acordo,
                                  acordo.cliente,
                                  acordo.validade.strftime('%d/%m/%Y')
                              ),
                              settings.EMAIL_HOST_USER,
                              [email_exec],
                              fail_silently=False)



        # for acordo in acordos:
        #     for colaborador in colaboradores:
        #         email_exec = colaborador.email
        #         if data_venc >= acordo.validade:
        #             send_mail('Vencimento do acordo {} está próximo'.format(acordo.acordo),
        #                       'O acordo {} do cliente {}, vence em {}, '
        #                       'favor deixar no radar'.format(
        #                           acordo.acordo,
        #                           acordo.cliente,
        #                           acordo.validade.strftime('%d/%m/%Y')
        #                       ),
        #                       settings.EMAIL_HOST_USER,
        #                       [email_exec],
        #                       fail_silently=False)
