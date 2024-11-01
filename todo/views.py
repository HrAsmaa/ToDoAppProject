from django.views import generic
from todo.models import Task


class ToDoListView(generic.ListView):
    template_name = "todo/list.html"
    context_object_name = "todo_items"

    def get_queryset(self):
        return Task.objects.all()

