from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('books', BooksView.as_view(), name='books'),
    path('books/<int:pk>', BookDetail.as_view()),
    path('authors', AuthorListCreateView.as_view(), name='authors'),
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('collections', BookCollectionView.as_view(), name='collections'),
    path('collections/<int:pk>', BookCollectionDetail.as_view()),
    path('search', GeneralSearchView.as_view()),
    path('qsearch', SearchView.as_view(), name='qsearch')
]
