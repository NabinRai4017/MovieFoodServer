from django.db import models

# Create your models here.
class Food(models.Model):

    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name