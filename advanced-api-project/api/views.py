from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer


# List and Create View for Books (read-only for unauthenticated users)
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books


# Update View for Books (only authenticated users can update)
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update book details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books


# Delete View for Books (only authenticated users can delete)
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books


# List and Create View for Books with filtering, searching, and ordering
class BookListView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating new books.
    Supports filtering by author and publication year,
    searching by title or author's name, and ordering by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Unauthenticated users can view books, but cannot create them

    # Enable filtering, searching, and ordering
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'publication_year']  # Enable filtering by author and publication year
    search_fields = ['title', 'author__name']  # Enable search by book title or author name
    ordering_fields = ['title', 'publication_year']  # Enable ordering by title or publication year


# Retrieve, Update, and Delete View for Individual Books
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting individual books by ID.
    Only authenticated users can modify or delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Unauthenticated users can view, but cannot modify or delete
    # books
