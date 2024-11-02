from django import forms
from todo.models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'startDate', 'limitDate']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'startDate' : forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'limitDate' : forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'startDate': 'Start Date',
            'limitDate': 'End Date'
        }