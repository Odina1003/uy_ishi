from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    images = models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name