from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import ClienteFilter
from .forms import ClienteForm
from .models import Cliente


@login_required
def list_cliente(request):
    clientes = Cliente.objects.filter(executivo__user=request.user)
    myFilter = ClienteFilter(request.GET, queryset=clientes)
    clientes = myFilter.qs

    return render(request, 'clientes.html', {'clientes': clientes, 'myFilter': myFilter})


@login_required
def new_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list_cliente')
    return render(request, 'cliente_form.html', {'form': form})


@login_required
def update_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')
    return render(request, 'cliente_form.html', {'form': form})


@login_required
def delete_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('list_cliente')
    return render(request, 'cliente_delete_confirm.html', {'cliente': cliente})
