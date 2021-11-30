from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.acordos_ae.models import AcordoAereo


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'index.html', data)

