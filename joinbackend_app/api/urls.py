from django.urls import path
from .views import contacts_view, tasks_view, users_view, subtasks_view

urlpatterns = [
    path('users/', users_view),
    path('contacts/', contacts_view),
    path('tasks/', tasks_view),
    path('subtasks/', subtasks_view),
]
