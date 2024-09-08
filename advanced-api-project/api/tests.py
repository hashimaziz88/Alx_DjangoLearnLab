from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITest(APITestCase):
    def setUp(self):
        """
        Set up test data for the Book and Author models.
        """
        author = Author.objects.create(name="Author Name")
        Book.objects.create(title="Book Title", publication_year=2023, author=author)

    def test_get_books(self):
        """
        Test listing books.
        """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        """
        Test creating a new book.
        """
        author = Author.objects.get(name="Author Name")
        data = {'title': 'New Book', 'publication_year': 2022, 'author': author.id}
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, 201)
