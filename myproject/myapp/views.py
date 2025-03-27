from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()  # Fetch all blog posts
    return render(request, 'myapp/home.html', {'posts': posts})