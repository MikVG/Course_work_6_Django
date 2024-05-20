from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogDetailView

app_name = BlogConfig.name


urlpatterns = [
    path('blog-list/', BlogListView.as_view(), name='blog-list'),
    path('blog-create', BlogCreateView.as_view(), name='blog-create'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]
