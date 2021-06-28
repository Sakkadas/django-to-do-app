from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

