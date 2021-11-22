from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import TarifarioFilter
from .models import Tarifario
from .forms import TarifarioForm


@login_required
def list_tarifario(request):
    tarifario = Tarifario.objects.all()

    myFilter = TarifarioFilter(request.GET, queryset=tarifario)
    tarifario = myFilter.qs

    return render(request, 'tarifario.html', {'tarifario': tarifario, 'myFilter': myFilter})


@login_required
def new_tarifario(request):
    form = TarifarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_tarifario')
    return render(request, 'tarifario_form.html', {'form': form})


@login_required
def update_tarifario(request, id):
    tarifario = get_object_or_404(Tarifario, pk=id)
    form = TarifarioForm(request.POST or None, instance=tarifario)

    if form.is_valid():
        form.save()
        return redirect('list_tarifario')
    return render(request, 'tarifario_form.html', {'form': form})


@login_required
def delete_tarifario(request, id):
    tarifario = get_object_or_404(Tarifario, pk=id)
    form = TarifarioForm(request.POST or None, instance=tarifario)

    if request.method == 'POST':
        tarifario.delete()
        return redirect('list_tarifario')
    return render(request, 'tarifario_delete_confirm.html', {'tarifario': tarifario})
