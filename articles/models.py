from django.db import models
from django_mysql.models import JSONField
from django.contrib.auth.models import User
def first():
    return {'foo': 'bar'}

# Create your models here.
class Article(models.Model):  
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, default="")
    body = models.TextField(max_length=3000, default="")
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='walk.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    attrs = JSONField(default=first)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'