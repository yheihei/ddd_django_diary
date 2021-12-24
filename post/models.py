from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=4096)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
