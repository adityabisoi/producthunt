from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField()
    votes = models.IntegerField(default=1)
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title

def limit(self):
    return self.body[:100]