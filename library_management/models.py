from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True, default=None)
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.name


class BookCollection(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, related_name='collection')
    def __str__(self):
        return self.name

