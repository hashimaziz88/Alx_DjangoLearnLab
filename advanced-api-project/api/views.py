from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer


# Create a new book
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'  # Optional template, can remove for API-only project
    success_url = reverse_lazy('book-list')

# Update an existing book
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

# Delete an existing book
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

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
