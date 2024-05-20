from random import sample

from blog.models import Blog
from mailing.models import SubscribeSettings, Client


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
