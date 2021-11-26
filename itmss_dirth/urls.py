from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('accounts/logout', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('acordos/', include('apps.acordos_ae.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('colaboradores/', include('apps.colaboradores.urls')),
    path('fees/', include('apps.fees.urls')),
    path('fornecedores/', include('apps.fornecedores.urls')),
    path('grupos/', include('apps.grupos.urls')),
    path('postos/', include('apps.postos.urls')),
    path('produtos/', include('apps.produtos.urls')),
    path('tarifarios/', include('apps.tarifarios.urls')),
]


