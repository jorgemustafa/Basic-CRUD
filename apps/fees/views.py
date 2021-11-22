from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeeForm
from .models import Fee


@login_required
def list_fee(request):
    fees = Fee.objects.all()
    return render(request, 'fee.html', {'fees': fees})


@login_required
def new_fee(request):
    form = FeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_fee')
    return render(request, 'fee_form.html', {'form': form})


@login_required
def update_fee(request, id):
    fee = get_object_or_404(Fee, pk=id)
    form = FeeForm(request.POST or None, instance=fee)

    if form.is_valid():
        form.save()
        return redirect('list_fee')
    return render(request, 'fee_form.html', {'form': form})


@login_required
def delete_fee(request, id):
    fee = get_object_or_404(Fee, pk=id)
    form = FeeForm(request.POST or None, instance=fee)

    if request.method == 'POST':
        fee.delete()
        return redirect('list_fee')
    return render(request, 'fee_delete_confirm.html', {'fee': fee})
