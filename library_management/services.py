from .serializers import *
from . models import *


def keyword_search(keyword, query):
    books = None
    if query == 'book':
        books = Book.objects.filter(name__icontains=keyword)
    elif query == 'author':
        books = Book.objects.filter(author__name__icontains=keyword)
    elif query == 'collection':
        books = Book.objects.filter(collection__name__icontains=keyword)
    return books
