from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import GrupoFilter
from .forms import GrupoForm
from .models import Grupo


@login_required
def list_grupo(request):
    grupo = Grupo.objects.all()
    myFilter = GrupoFilter(request.GET, queryset=grupo)
    grupo = myFilter.qs

    return render(request, 'grupo.html', {'grupo': grupo, 'myFilter': myFilter})


@login_required
def new_grupo(request):
    form = GrupoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_grupo')
    return render(request, 'grupo_form.html', {'form': form})


@login_required
def update_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    form = GrupoForm(request.POST or None, instance=grupo)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list_grupo')
    return render(request, 'grupo_form.html', {'form': form})


@login_required
def delete_grupo(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    form = GrupoForm(request.POST or None, instance=grupo)

    if request.method == 'POST':
        grupo.delete()
        return redirect('list_grupo')
    return render(request, 'grupo_delete_confirm.html', {'grupo': grupo})
