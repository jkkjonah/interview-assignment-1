from django.db import models


class CalendarEvent(models.Model):
    """
    A calenar event
    """

    datetime = models.DateTimeField()


class Task(models.Model):
    """
    A task in the TODO list
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE, null=True, blank=True)


class TaskLabel(models.Model):
    """
    Label for task
    """

    name = models.CharField(max_length=100)
    tasks = models.ManyToManyField(Task)
