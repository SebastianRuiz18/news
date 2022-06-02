from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=96)
    description = models.TextField()

    def __str__(self):
        return self.name
        