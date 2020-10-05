from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), required=False)
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1


class BookCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCollection
        fields = '__all__'
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        