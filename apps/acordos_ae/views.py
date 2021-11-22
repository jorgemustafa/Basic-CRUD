from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.acordos_ae.models import AcordoAereo
from .forms import AcordoForm, AcordoFormGol
from ..fornecedores.models import Fornecedor


@login_required
def list_acordo(request):
    acordo = AcordoAereo.objects.all()
    return render(request, 'acordos.html', {'acordo': acordo})


@login_required
def new_acordo(request, fornecedor):
# def new_acordo(request, fornecedor, pk):

    # formteste = get_object_or_404(Fornecedor, pk=pk)

    if fornecedor == 'gol':
        form = AcordoFormGol(request.POST or None)
        print('Forn É GOL!')

    else:
        form = AcordoForm(request.POST or None)
        print('Forn não é GOL')

    form.fornecedores = fornecedor

    if form.is_valid():
        form.save()
        print('Form é Válido')
        return redirect('list_acordo')

    print('Form Invalido')
    # return render(request, 'acordo_form.html', {'form': form, 'fornecedor': fornecedor, 'formteste': formteste})
    return render(request, 'acordo_form.html', {'form': form, 'fornecedor': fornecedor})


@login_required
def update_acordo(request, id):
    acordo = get_object_or_404(AcordoAereo, pk=id)
    form = AcordoForm(request.POST or None, instance=acordo)

    if form.is_valid():
        form.save()
        return redirect('list_acordo')
    return render(request, 'acordo_form.html', {'form': form})


@login_required
def delete_acordo(request, id):
    acordo = get_object_or_404(AcordoAereo, pk=id)
    form = AcordoForm(request.POST or None, instance=acordo)

    if request.method == 'POST':
        acordo.delete()
        return redirect('list_acordo')
    return render(request, 'acordo_delete_confirm.html', {'acordo': acordo})


def select_fornecedor(request):
    fornecedor = Fornecedor.objects.all()
    return render(request, 'select_fornecedor.html', {'fornecedor': fornecedor})
