from django.urls import path
from .views import *


urlpatterns = [
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('api/genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('api/genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/genres/<int:genre_id>/export/', ExportBooksAPIView.as_view(), name='export-books'),
    path('signin/',signin),
    path('allapi/',api)
]

