from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)

def __str__(self):
    return f'{self.id} {self.title}'



