from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, MessageListView, SubscribeListView, SubscribeCreateView, \
    MessageCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', SubscribeListView.as_view(), name='home'),
    path('subscribe_create/', SubscribeCreateView.as_view(), name='subscribe_create'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
]
