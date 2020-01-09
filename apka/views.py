from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


def home(request):

    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    template_name = 'home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def kontakt(request):
    return render(request, 'kontakt.html', {'title': 'Kontakt'})
