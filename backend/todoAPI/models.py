from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    priority = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    finish_by = models.DateField()
    completed = models.BooleanField(default=False)
