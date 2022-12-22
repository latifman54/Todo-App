from django.views.generic import TemplateView, ListView, View, CreateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
# from .forms import TaskForm

class WelcomePage(TemplateView):
    template_name = 'main.html'

class HomeListView(ListView):
    model = Task
    template_name = 'homepage.html'
    context_object_name = 'tasks'
    ordering = ['-date_added']

class CompleteTaskView(ListView):
    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        task.completed = True
        task.save()
        return redirect('todo-home')

# class AddTaskView(View):
#     def post(self, request):
#         title = request.POST['title']
#         task = Task(title=title)
#         task.save()
#         return redirect('todo-home')

class CreateTaskView(CreateView):
    model = Task
    template_name = 'create_task.html'
    fields = ['title']
    success_url = reverse_lazy('todo-home')


