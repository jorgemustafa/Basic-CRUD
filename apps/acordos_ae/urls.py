from django.urls import path
from .views import list_acordo, new_acordo, update_acordo, delete_acordo

urlpatterns = [
    path('list/', list_acordo, name='list_acordo'),
    path('new/', new_acordo, name='new_acordo'),
    path('update/<int:id>/', update_acordo, name='update_acordo'),
    path('delete/<int:id>/', delete_acordo, name='delete_acordo'),
]