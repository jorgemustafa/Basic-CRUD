from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .filters import FeeFilter
from .forms import FeeForm
from .models import Fee


@login_required
def list_fee(request):
    fees = Fee.objects.filter(cliente__executivo__user=request.user)

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


# def media_fee(request):
#     taxas = Fee.int(
#                 Fee.aenacon + Fee.aeinton + Fee.honacon + Fee.hointon + Fee.canacon + Fee.cainton + Fee.aenacoff + Fee.aeintoff + Fee.honacoff + Fee.hointoff + Fee.canacoff + \
#                 Fee.caintoff + Fee.vip + Fee.doc + Fee.fer + Fee.emergencial + Fee.ateae + Fee.segViagem + Fee.passRod + Fee.reembolso + Fee.cancelamento + Fee.assentoConf \
#                 + Fee.implantacao + Fee.treinamento + Fee.consultoria + Fee.expense + Fee.eventos + Fee.demais
#     )
