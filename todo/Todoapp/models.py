from django.db import models

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=200)
    due_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    status = models.BooleanField()