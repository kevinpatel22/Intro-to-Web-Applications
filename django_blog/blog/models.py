from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    draft = models.BooleanField()
    body = models.TextField(validators=[MinLengthValidator(1)])
    published_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return f'{self.id} {self.title}'

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')



