from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView

app_name = BlogConfig.name


urlpatterns = [
    path('blog-list/', BlogListView.as_view(), name='blog-list'),
    path('blog-create', BlogCreateView.as_view(), name='blog-create'),
    path('blog-detail/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog-detail'),
]
