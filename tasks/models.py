from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Task title
    completed = models.BooleanField(default=False)  # Task status (completed or not)

    def __str__(self):
        return self.title
