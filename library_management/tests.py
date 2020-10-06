from rest_framework.test import APITestCase
from django.urls import reverse
from .models import *


class TestBookView(APITestCase):

    def setUp(self):
        self.url = reverse('books')
        author = Author.objects.create(name="dummyauthor")
        self.book_data = {
            "name": "bookname",
            "author": author.id
        }

    def tearDown(self):
        del self.url
        del self.book_data

    def test_book_not_created(self):
        respone = self.client.post(self.url)
        self.assertEqual(respone.status_code, 400)

    def test_book_created(self):
        respone = self.client.post(
            self.url, data=self.book_data, format="json")
        self.assertEqual(respone.status_code, 201)


class TestAuthorView(APITestCase):

    def setUp(self):
        self.url = reverse('authors')

        self.author_data = {
            "name": "authorname"
        }

    def tearDown(self):
        del self.url
        del self.author_data

    def test_author_not_created(self):
        respone = self.client.post(self.url)
        self.assertEqual(respone.status_code, 400)

    def test_author_created(self):
        respone = self.client.post(
            self.url, data=self.author_data, format="json")
        self.assertEqual(respone.status_code, 201)


class TestCollectionView(APITestCase):

    def setUp(self):
        self.url = reverse('collections')
        author = Author.objects.create(name="dummyauthor")
        book = Book.objects.create(name="dummybook", author=author)
        self.collection_data = {
            "name": "collection name",
            "books": book.id
        }

    def tearDown(self):
        del self.url
        del self.collection_data

    def test_collection_not_created(self):
        respone = self.client.post(self.url)
        self.assertEqual(respone.status_code, 400)

    def test_collection_created(self):
        respone = self.client.post(
            self.url, data=self.collection_data, format="json")
        self.assertEqual(respone.status_code, 201)


class TestSearchView(APITestCase):
    def setUp(self):
        self.url = reverse('qsearch')
        author = Author.objects.create(name="dummyauthor")
        self.book = Book.objects.create(name="dummybook", author=author)
        collection = BookCollection.objects.create(name="dummycollection")
        collection.books.add(self.book)

    def tearDown(self):
        del self.url

    def test_book_search(self):
        respone = self.client.get(
            self.url, data={"q": "book", "keyword": "dummy"})
        self.assertEqual(respone.status_code, 200)
        self.assertEqual(respone.data["books"][0]["name"], self.book.name)

    def test_author_search(self):
        respone = self.client.get(
            self.url, data={"q": "author", "keyword": "dummyauthor"})
        self.assertEqual(respone.status_code, 200)
        self.assertEqual(respone.data["books"][0]["name"], self.book.name)

    def test_collection_search(self):
        respone = self.client.get(
            self.url, data={"q": "collection", "keyword": "dummycollection"})
        self.assertEqual(respone.status_code, 200)
        self.assertEqual(respone.data["books"][0]["name"], self.book.name)
