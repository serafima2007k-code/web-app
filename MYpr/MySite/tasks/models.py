from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# Create your models here.
