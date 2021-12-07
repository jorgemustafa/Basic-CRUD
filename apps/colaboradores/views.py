from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import ColaboradorFilter
from .forms import ColaboradorForm
from .models import Colaborador


@login_required
def list_colaborador(request):
    colaboradores = Colaborador.objects.all()
    myFilter = ColaboradorFilter(request.GET, queryset=colaboradores)
    colaboradores = myFilter.qs

    return render(request, 'colaborador.html', {'colaboradores': colaboradores, 'myFilter': myFilter})


@login_required
def new_colaborador(request):
    form = ColaboradorForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list_colaborador')
    return render(request, 'colaborador_form.html', {'form': form})


@login_required
def update_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    form = ColaboradorForm(request.POST or None, instance=colaborador)

    if form.is_valid():
        form.save()
        return redirect('list_colaborador')
    return render(request, 'colaborador_form.html', {'form': form})


@login_required
def delete_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    form = ColaboradorForm(request.POST or None, instance=colaborador)

    if request.method == 'POST':
        colaborador.delete()
        return redirect('list_colaborador')
    return render(request, 'colaborador_delete_confirm.html', {'colaborador': colaborador})

# def settings_colaborador(request,pk):
#         colaboradores = get_object_or_404(Colaborador, pk=pk)
#         return render(request, 'info_user.html', {'colaboradores': colaboradores})
