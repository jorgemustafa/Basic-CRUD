from django.urls import path
from .views import list_fee, new_fee, update_fee, delete_fee


urlpatterns = [
    path('list/', list_fee, name='list_fee'),
    path('new/', new_fee, name='new_fee'),
    path('update/<int:pk>/', update_fee, name='update_fee'),
    path('delete/<int:pk>/', delete_fee, name='delete_fee'),
]