from django.urls import path
from . import views

app_name = "todo"
urlpatterns =[
    path('', views.ToDoListView.as_view(), name="todo_list")
]