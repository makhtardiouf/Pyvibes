
from django.db import models
''' DB tables for the Blogging mimic '''

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateField()
    updated = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()

    def __str__(self):              
        return self.headline


