from django.db import models


# Create your models here.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
