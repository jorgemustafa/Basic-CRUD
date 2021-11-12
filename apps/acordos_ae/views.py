from django.shortcuts import render, redirect, get_object_or_404
from apps.acordos_ae.models import AcordoAereo
from .forms import AcordoForm


def list_acordo(request):
    acordo = AcordoAereo.objects.all()
    return render(request, 'acordos.html', {'acordo': acordo})


def new_acordo(request):
    form = AcordoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_acordo')
    return render(request, 'acordo_form.html', {'form': form})


def update_acordo(request, id):
    acordo = get_object_or_404(AcordoAereo, pk=id)
    form = AcordoForm(request.POST or None, instance=acordo)

    if form.is_valid():
        form.save()
        return redirect('list_acordo')
    return render(request, 'acordo_form.html', {'form': form})


def delete_acordo(request, id):
    acordo = get_object_or_404(AcordoAereo, pk=id)
    form = AcordoForm(request.POST or None, instance=acordo)

    if request.method == 'POST':
        acordo.delete()
        return redirect('list_acordo')
    return render(request, 'acordo_delete_confirm.html', {'acordo': acordo})
