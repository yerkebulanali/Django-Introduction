from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):

    #books = Book.objects.all()
    #books = Book.objects.filter(is_published=True)

    book = Book.objects.get(id=2)
    output = f'We have {book.title} book with id {book.id} <br>'

    #for book in books:
        #output += f'We have {book.title} book with id {book.id} <br>'
    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First message from views')