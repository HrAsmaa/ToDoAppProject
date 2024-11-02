
from django.db import models
from django.urls import reverse


class Task(models.Model):
    """" Model representing a toDo item"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    startDate = models.DateTimeField()
    limitDate = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo:todo_list')



