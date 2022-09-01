from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)

    def __str__(self):
        return self.title

