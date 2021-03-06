from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, get_object_or_404, \
    RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .services import keyword_search


class BooksView(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetail(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class AuthorListCreateView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetail(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class BookCollectionView(APIView):
    def get(Self, request):
        queryset = BookCollection.objects.all()
        serializer = BookCollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookCollectionSerializer(data=request.data)
        if serializer.is_valid():
            collection = serializer.save()
            try:
                books = request.data['books'].split(',')
                for book in books:
                    collection.books.add(int(book))
            except:
                pass
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookCollectionDetail(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(BookCollection, pk=pk)
        serializer = BookCollectionSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(BookCollection, pk=pk)
        serializer = BookCollectionSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GeneralSearchView(APIView):
    def get(self, request):
        keyword = request.GET.get('keyword')
        books = Book.objects.filter(name__icontains=keyword)
        collections = BookCollection.objects.filter(name__icontains=keyword)
        authors = Author.objects.filter(name__icontains=keyword)
        return Response({
                        "books": BookSerializer(books, many=True).data,
                        "collections": BookCollectionSerializer(
                            collections, many=True).data,
                        "Authors": AuthorSerializer(authors, many=True).data
                        })


class SearchView(APIView):
    def get(self, request):
        result = keyword_search(request.GET.get(
            'keyword'), request.GET.get('q'))
        if result:
            return Response({"books": BookSerializer(result, many=True).data},
                            status=200)
        else:
            return Response({
                "Enter a valid query attribute"
            }, status=400)
