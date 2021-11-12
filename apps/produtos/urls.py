from django.urls import path
from .views import list_produto, new_produto, update_produto, delete_produto

urlpatterns = [
    path('list/', list_produto, name='list_produto'),
    path('new/', new_produto, name='new_produto'),
    path('update/<int:id>/', update_produto, name='update_produto'),
    path('delete/<int:id>/', delete_produto, name='delete_produto'),
]