from relationship_app.models import Author, Book, Library, Librarian


Library = Library.objects.get(name=library_name)
books_in_library = Library.books.all()
