from django.db import models


# Create your models here.
class Allergy(models.Model):
    content = models.CharField(max_length=100)
    checked = models.BooleanField()

    def __str__(self):
        return self.content


class Etc(models.Model):
    content = models.CharField(max_length=100)
    checked = models.BooleanField()

    def __str__(self):
        return self.content
