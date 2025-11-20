from django.db import models

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    badge_image = models.ImageField()
