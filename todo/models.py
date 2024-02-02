from django.db import models
class Todo(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(null=True, blank=True) 
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
