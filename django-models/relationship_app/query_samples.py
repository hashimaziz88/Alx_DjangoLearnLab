from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name="Library Name")
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
