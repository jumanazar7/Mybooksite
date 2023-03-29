from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', BooksListView.as_view(), name="list"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="detail"),
    path('add/', BookCreateView.as_view(), name="add_book"),
    path('update/<int:pk>/', BookUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name="delete"),
    path('add/genre/', add_genres, name="add_genre"),
    path('add/author/', add_author, name="add_author"),
]
