from django.db import models
import os
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', null = True, blank=True)

    def __str__(self):
        return f"Post: {self.title}"

# class image(models.Model):
#     file = models.ImageField(upload_to='images/')
#     title = models.CharField(max_length=200)
#     body = models.TextField()