from django.urls import path
from .views import list_books, LibraryDetailView
# relationship_app/urls.py
from django.urls import path
from .views import RegisterView, LoginView, LogoutView





urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
