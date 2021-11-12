from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def list_produto(request):
    produto = Produto.objects.all()
    return render(request, 'produto.html', {'produto': produto})

def new_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_produto')
    return render(request, 'produto_form.html', {'form': form})

def update_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('list_produto')
    return render(request, 'produto_form.html', {'form': form})

def delete_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('list_produto')
    return render(request, 'acordo_delete_confirm.html', {'produto': produto})

