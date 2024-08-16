from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
# relationship_app/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Helper functions for role checks
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin View
class AdminView(LoginRequiredMixin, View):
    def get(self, request):
        if not is_admin(request.user):
            return render(request, '403.html')  # Use a 403 template or redirect as needed
        return render(request, 'relationship_app/admin_view.html')

# Librarian View
class LibrarianView(LoginRequiredMixin, View):
    def get(self, request):
        if not is_librarian(request.user):
            return render(request, '403.html')  # Use a 403 template or redirect as needed
        return render(request, 'relationship_app/librarian_view.html')

# Member View
class MemberView(LoginRequiredMixin, View):
    def get(self, request):
        if not is_member(request.user):
            return render(request, '403.html')  # Use a 403 template or redirect as needed
        return render(request, 'relationship_app/member_view.html')

# Custom LoginView
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        return render(request, 'relationship_app/login.html', {'form': form})


# Custom LogoutView
class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect('login')  # Redirect to login page after logout


# RegisterView remains the same
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
# Create your views here.
