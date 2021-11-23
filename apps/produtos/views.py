from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import ProdutoFilter
from .models import Produto
from .forms import ProdutoForm


@login_required
def list_produto(request):
    produto = Produto.objects.all()

    myFilter = ProdutoFilter(request.GET, queryset=produto)
    produto = myFilter.qs

    return render(request, 'produto.html', {'produto': produto, 'myFilter': myFilter})


@login_required
def new_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list_produto')
    return render(request, 'produto_form.html', {'form': form})


@login_required
def update_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('list_produto')
    return render(request, 'produto_form.html', {'form': form})


@login_required
def delete_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('list_produto')
    return render(request, 'produto_delete_confirm.html', {'produto': produto})
