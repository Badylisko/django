from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView


def home(request):

    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    template_name = 'home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def kontakt(request):
    return render(request, 'kontakt.html', {'title': 'Kontakt'})
