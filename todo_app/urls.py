from django.urls import path
from .views import WelcomePage, HomeListView, CompleteTaskView, CreateTaskView

urlpatterns = [
    path('', WelcomePage.as_view(), name='todo-welcome'),
    path('tasks', HomeListView.as_view(), name='todo-home'),
    path('create/', CreateTaskView.as_view(), name='todo-create_task'),
    path('complete/<int:task_id>', CompleteTaskView.as_view(), name='todo-complete_task'),
]
