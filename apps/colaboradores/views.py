from django.shortcuts import render, redirect, get_object_or_404
from .forms import ColaboradorForm
from .models import Colaborador


def list_colaborador(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaborador.html', {'colaboradores': colaboradores})


def new_colaborador(request):
    form = ColaboradorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_colaborador')
    return render(request, 'colaborador_form.html', {'form': form})


def update_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm(request.POST or None, instance=colaborador)

    if form.is_valid():
        form.save()
        return redirect('list_colaborador')
    return render(request, 'colaborador_form.html', {'form': form})

def delete_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm(request.POST or None, instance=colaborador)

    if request.method == 'POST':
        colaborador.delete()
        return redirect('list_colaborador')
    return render(request, 'colaborador_delete_confirm.html', {'colaborador': colaborador})
