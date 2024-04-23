from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.ImageField(upload_to='assets/', null=True, blank=True)
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
