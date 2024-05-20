from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, MessageListView, SubscribeListView, SubscribeCreateView, \
    MessageCreateView, SubscribeUpdateView, SubscribeDeleteView, SubscribeDetailView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView, MessageDetailView, MessageUpdateView, MessageDeleteView, main

app_name = MailingConfig.name

urlpatterns = [
    path('', main, name='main'),
    path('subscribe_list', SubscribeListView.as_view(), name='subscribe_list'),
    path('subscribe_create/', SubscribeCreateView.as_view(), name='subscribe_create'),
    path('subscribe_detail/<int:pk>/', SubscribeDetailView.as_view(), name='subscribe_detail'),
    path('subscribe_edit/<int:pk>/', SubscribeUpdateView.as_view(), name='subscribe_edit'),
    path('subscribe_delete/<int:pk>/', SubscribeDeleteView.as_view(), name='subscribe_delete'),

    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('message_list/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]
