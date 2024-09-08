from django.urls import path
from .views import BookListView, BookDetailView
from .views import BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List and create books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, update, delete by ID
    path('books/new/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
