from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(ListView):
    model = Blog


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
