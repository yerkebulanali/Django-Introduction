from rest_framework import serializers
from .models import Book, BookNumber


class BookNumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']
class BookSerializers(serializers.ModelSerializer):
    number = BookNumberSerializers(many=False)
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number']

