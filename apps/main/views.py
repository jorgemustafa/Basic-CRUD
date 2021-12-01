from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.clientes.models import Cliente
from apps.colaboradores.models import Colaborador
from apps.fees.models import Fee
from apps.produtos.models import Produto


@login_required
def home(request):
    clientes = Cliente.objects.all()
    fees = Fee.objects.all()
    cont_clientes = Cliente.objects.count()
    cont_colaboradores = Colaborador.objects.count()
    cont_produtos = Produto.objects.count()
    data = {}
    data['usuario'] = request.user
    return render(request, 'index.html', {'data': data, 'clientes': clientes, 'cont_clientes': cont_clientes, 'cont_colaboradores': cont_colaboradores, 'cont_produtos': cont_produtos, 'fees': fees})
