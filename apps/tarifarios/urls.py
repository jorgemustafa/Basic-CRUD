from django.urls import path
from .views import list_tarifario, new_tarifario, update_tarifario, delete_tarifario

urlpatterns = [
    path('list/', list_tarifario, name='list_tarifario'),
    path('new/', new_tarifario, name='new_tarifario'),
    path('update/<int:pk>/', update_tarifario, name='update_tarifario'),
    path('delete/<int:pk>/', delete_tarifario, name='delete_tarifario'),
]