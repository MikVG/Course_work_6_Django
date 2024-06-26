from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from blog.forms import BlogForm
from blog.models import Blog
from blog.services import get_blog_from_cache


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return get_blog_from_cache()


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog-list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object
