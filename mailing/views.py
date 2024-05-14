from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.forms import ClientForm, SubscribeForm, MessageForm
from mailing.models import Message, Client, SubscribeSettings


class SubscribeListView(ListView):
    model = SubscribeSettings


class SubscribeCreateView(CreateView):
    model = SubscribeSettings
    form_class = SubscribeForm
    success_url = reverse_lazy('mailing:home')


class SubscribeDetailView(DetailView):
    model = SubscribeSettings


class SubscribeUpdateView(UpdateView):
    model = SubscribeSettings
    form_class = SubscribeForm
    success_url = reverse_lazy('mailing:home')


class SubscribeDeleteView(DeleteView):
    model = SubscribeSettings
    success_url = reverse_lazy('mailing:home')


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
