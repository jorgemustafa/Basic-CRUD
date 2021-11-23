from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import FornecedorFilter
from .forms import FornecedorForm
from .models import Fornecedor


@login_required
def list_fornecedor(request):
    fornecedor = Fornecedor.objects.all()

    myFilter = FornecedorFilter(request.GET, queryset=fornecedor)
    fornecedor = myFilter.qs

    return render(request, 'fornecedor.html', {'fornecedor': fornecedor, 'myFilter': myFilter})


@login_required
def new_fornecedor(request):
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor_form.html', {'form': form})


@login_required
def update_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor_form.html', {'form': form})


@login_required
def delete_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor_delete_confirm.html', {'fornecedor': fornecedor})
