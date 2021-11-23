from django.urls import path
from .views import list_posto, new_posto, update_posto, delete_posto

urlpatterns = [
    path('list/', list_posto, name='list_posto'),
    path('new/', new_posto, name='new_posto'),
    path('update/<int:pk>/', update_posto, name='update_posto'),
    path('delete/<int:pk>/', delete_posto, name='delete_posto'),
]