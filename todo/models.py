from django.db import models

# Create your models here.


class Todomodel(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)