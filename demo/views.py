from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializers

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = Book.objects.all()