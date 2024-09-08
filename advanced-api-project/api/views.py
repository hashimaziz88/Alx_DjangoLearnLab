from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# List and Create View for Books (read-only for unauthenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books


# Update View for Books (only authenticated users can update)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books


# Delete View for Books (only authenticated users can delete)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books


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
