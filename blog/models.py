from django.db import models
from datetime import datetime

# Create your models here.

# Post
class post(models.Model):
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,blank=True)
    banner = models.ImageField(upload_to='images/banners',blank=True)
    author = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField('Creation Date', default=datetime.now)
    TYPE_CHOICES = (
        (1, 'Page'),# Included in menu
        (2, 'Article'),# Listed on articles page
    )
    type = models.CharField(max_length=9, choices=TYPE_CHOICES, default='1')
    def __str__(self):
        return self.title