from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

class PostView(generic.DetailView):
    model = Post
    template = 'blog.html'
