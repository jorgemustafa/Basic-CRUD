from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import FeeFilter
from .forms import FeeForm
from .models import Fee


@login_required
def list_fee(request):
    fees = Fee.objects.all()

    myFilter = FeeFilter(request.GET, queryset=fees)
    fees = myFilter.qs

    return render(request, 'fee.html', {'fees': fees, 'myFilter': myFilter})


@login_required
def new_fee(request):
    form = FeeForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('list_fee')
    return render(request, 'fee_form.html', {'form': form})


@login_required
def update_fee(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    form = FeeForm(request.POST or None, instance=fee)

    if form.is_valid():
        form.save()
        return redirect('list_fee')
    return render(request, 'fee_form.html', {'form': form})


@login_required
def delete_fee(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    form = FeeForm(request.POST or None, instance=fee)

    if request.method == 'POST':
        fee.delete()
        return redirect('list_fee')
    return render(request, 'fee_delete_confirm.html', {'fee': fee})
