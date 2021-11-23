from django.urls import path
from .views import list_grupo, new_grupo, update_grupo, delete_grupo

urlpatterns = [
    path('list/', list_grupo, name='list_grupo'),
    path('new/', new_grupo, name='new_grupo'),
    path('update/<int:pk>/', update_grupo, name='update_grupo'),
    path('delete/<int:pk>/', delete_grupo, name='delete_grupo'),
]