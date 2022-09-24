from django.contrib import admin
from .models import Book, BookNumber

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', "description", 'price']
    list_filter = ['published']
    search_fields = ['title']

admin.site.register(BookNumber)