from django.shortcuts import render, redirect, get_object_or_404
from .forms import FornecedorForm
from .models import Fornecedor


def list_fornecedor(request):
    fornecedor = Fornecedor.objects.all()
    return render(request, 'fornecedor.html', {'fornecedores': fornecedor})

def new_fornecedor(request):
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor_form.html', {'form': form})

def update_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if form.is_valid():
        form.save()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor_form.html', {'form': form})

def delete_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect('list_fornecedor')
    return render(request, 'fornecedor_delete_confirm.html', {'fornecedor': fornecedor})