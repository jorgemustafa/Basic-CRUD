from django.urls import path
from .views import list_fornecedor, new_fornecedor, update_fornecedor, delete_fornecedor


urlpatterns = [
    path('list/', list_fornecedor, name='list_fornecedor'),
    path('new/', new_fornecedor, name='new_fornecedor'),
    path('update/<int:id>/', update_fornecedor, name='update_fornecedor'),
    path('delete/<int:id>/', delete_fornecedor, name='delete_fornecedor'),
]