from django.urls import path
from .views import list_colaborador, new_colaborador, update_colaborador, delete_colaborador

urlpatterns = [
    path('list/', list_colaborador, name='list_colaborador'),
    path('new/', new_colaborador, name='new_colaborador'),
    path('update/<int:id>/', update_colaborador, name='update_colaborador'),
    path('delete/<int:id>/', delete_colaborador, name='delete_colaborador'),
]