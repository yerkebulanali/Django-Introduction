from rest_framework import serializers
from .models import Book, BookNumber, Character


class BookNumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']
class CharacterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

class BookSerializers(serializers.ModelSerializer):
    number = BookNumberSerializers(many=False)
    characters = CharacterSerializers(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'published', 'is_published', 'number', 'characters']

