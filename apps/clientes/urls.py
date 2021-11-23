from django.urls import path
from .views import list_cliente, new_cliente, update_cliente, delete_cliente

urlpatterns = [
    path('list/', list_cliente, name='list_cliente'),
    path('new/', new_cliente, name='new_cliente'),
    path('update/<int:pk>/', update_cliente, name='update_cliente'),
    path('delete/<int:pk>/', delete_cliente, name='delete_cliente'),
]