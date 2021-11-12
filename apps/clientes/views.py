from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente


def list_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'clientes.html', {'cliente': cliente})


def new_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')
    return render(request, 'cliente_form.html', {'form': form})


def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')
    return render(request, 'cliente_form.html', {'form': form})


def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('list_cliente')
    return render(request, 'cliente_delete_confirm.html', {'cliente': cliente})
