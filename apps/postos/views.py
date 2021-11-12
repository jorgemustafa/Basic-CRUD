from django.shortcuts import render, redirect, get_object_or_404
from .models import POS
from .forms import PostoForm


def list_posto(request):
    posto = POS.objects.all()
    return render(request, 'posto.html', {'postos': posto})

def new_posto(request):
    form = PostoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_posto')
    return render(request, 'posto_form.html', {'form': form})

def update_posto(request, id):
    posto = get_object_or_404(POS, pk=id)
    form = PostoForm(request.POST or None, instance=posto)

    if form.is_valid():
        form.save()
        return redirect('list_posto')
    return render(request, 'posto_form.html', {'form': form})

def delete_posto(request, id):
    posto = get_object_or_404(POS, pk=id)
    form = PostoForm(request.POST or None, instance=posto)

    if request.method == 'POST':
        posto.delete()
        return redirect('list_posto')
    return render(request, 'posto_delete_confirm.html', {'posto': posto})