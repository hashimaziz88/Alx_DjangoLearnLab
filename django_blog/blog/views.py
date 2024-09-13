from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
