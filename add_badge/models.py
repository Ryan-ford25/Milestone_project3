from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    badge_image = models.ImageField()

    def __str__(self):
        return f"{self.name} badge"


class BadgeRequirements(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name = "requirements")
    description = models.CharField(max_length = 255)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.badge.name} - Requirement {self.order}"
    
    class Meta:
        ordering = ["order"]