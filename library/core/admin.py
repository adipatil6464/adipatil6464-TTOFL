from django.contrib import admin
from .models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'city', 'author_id')
    search_fields = ('name', 'email')
    list_filter = ('city',)
    ordering = ('id',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'num_pages')
    search_fields = ('title', 'author__name')
    list_filter = ('genre', 'author')
    ordering = ('id',)
