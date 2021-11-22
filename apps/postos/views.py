from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import POSFilter
from .models import POS
from .forms import PostoForm


@login_required
def list_posto(request):
    posto = POS.objects.all()

    myFilter = POSFilter(request.GET, queryset=posto)
    posto = myFilter.qs

    return render(request, 'posto.html', {'postos': posto, 'myFilter': myFilter})


@login_required
def new_posto(request):
    form = PostoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_posto')
    return render(request, 'posto_form.html', {'form': form})


@login_required
def update_posto(request, id):
    posto = get_object_or_404(POS, pk=id)
    form = PostoForm(request.POST or None, instance=posto)

    if form.is_valid():
        form.save()
        return redirect('list_posto')
    return render(request, 'posto_form.html', {'form': form})


@login_required
def delete_posto(request, id):
    posto = get_object_or_404(POS, pk=id)
    form = PostoForm(request.POST or None, instance=posto)

    if request.method == 'POST':
        posto.delete()
        return redirect('list_posto')
    return render(request, 'posto_delete_confirm.html', {'posto': posto})
