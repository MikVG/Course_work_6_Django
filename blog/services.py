from random import sample

from django.core.cache import cache

from blog.models import Blog
from mailing.models import SubscribeSettings, Client

from config.settings import CACHE_ENABLED

def main_page():
    mailing_count = SubscribeSettings.objects.all().count
    mailing_active_count = SubscribeSettings.objects.all().filter(status__in=['created', 'started']).count()
    client_count = Client.objects.all().count
    queryset_all = Blog.objects.all()
    if queryset_all:
        queryset = sample(list(queryset_all), 3)
    else:
        queryset = None

    context = {
        'mailing_count': mailing_count,
        'mailing_active_count': mailing_active_count,
        'client_count': client_count,
        'queryset': queryset,
    }
    return context


def get_blog_from_cache():
    if not CACHE_ENABLED:
        return Blog.objects.all()
    key = "blog_list"
    blogs = cache.get(key)
    if blogs is not None:
        return blogs
    blogs = Blog.objects.all()
    cache.set(key, blogs)
    return blogs
