from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating new books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    """
    Only allow authenticated users to create new books.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting individual books by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
