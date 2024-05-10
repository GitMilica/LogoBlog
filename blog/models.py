from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Post(models.Model):
    slug = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    image = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title