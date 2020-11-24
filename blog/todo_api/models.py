from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS = (
        ('todo', 'TODO'),
        ('done', 'DONE')
    )
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS, default='todo')
