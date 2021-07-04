from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class todoList(models.Model):
    title = models.CharField(default="", max_length=20)
    start_date = models.DateField()
    update = models.DateField(auto_now=True)
    com_date = models.DateField()
    content = models.TextField(default="")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title