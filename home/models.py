from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField()
    content = models.TextField()
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title
