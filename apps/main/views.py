from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.acordos_ae.models import AcordoAereo
from apps.clientes.models import Cliente
from apps.colaboradores.models import Colaborador
from apps.fees.models import Fee
from apps.tarifarios.models import Tarifario


@login_required
def home(request):
    clientes = Cliente.objects.all()
    fees = Fee.objects.all()
    cont_clientes = Cliente.objects.count()
    cont_acordosae = AcordoAereo.objects.count()
    cont_tarifarios = Tarifario.objects.count()
    colaboradores = Colaborador.objects.filter(user=request.user.id)
    data = {}
    data['usuario'] = request.user

    return render(request, 'index.html', {'data': data, 'clientes': clientes,
    'cont_clientes': cont_clientes, 'cont_acordosae': cont_acordosae,
    'cont_tarifarios': cont_tarifarios, 'fees': fees, 'colaboradores': colaboradores})