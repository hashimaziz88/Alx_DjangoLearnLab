from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone  # Importing timezone to handle publication year validation


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model, including custom validation to ensure
    the publication year is not set in the future.
    """

    class Meta:
        model = Book
        fields = ['title', 'publication_year']

    def validate_publication_year(self, value):
        """
        Ensure that the publication year is not in the future.
        """
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested serializer for the books written by the author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
