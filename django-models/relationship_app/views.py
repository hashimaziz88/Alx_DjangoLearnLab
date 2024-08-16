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

# Custom LoginView
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        return render(request, 'login.html', {'form': form})

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
