from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.services import main_page
from mailing.forms import ClientForm, SubscribeForm, MessageForm, SubscribeManagerForm
from mailing.models import Message, Client, SubscribeSettings


@login_required
def main(request):
    context = main_page()
    return render(request, 'mailing/main.html', context)


class SubscribeListView(ListView):
    model = SubscribeSettings


class SubscribeCreateView(LoginRequiredMixin, CreateView):
    model = SubscribeSettings
    form_class = SubscribeForm
    success_url = reverse_lazy('mailing:subscribe_list')

    def form_valid(self, form):
        subscribe = form.save()
        user = self.request.user
        subscribe.owner = user
        subscribe.save()
        return super().form_valid(form)


class SubscribeDetailView(LoginRequiredMixin, DetailView):
    model = SubscribeSettings


class SubscribeUpdateView(LoginRequiredMixin, UpdateView):
    model = SubscribeSettings
    form_class = SubscribeForm
    success_url = reverse_lazy('mailing:subscribe_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return SubscribeForm
        if user.has_perm('mailing.can_subscribe_off'):
            return SubscribeManagerForm
        raise PermissionDenied


class SubscribeDeleteView(LoginRequiredMixin, DeleteView):
    model = SubscribeSettings
    success_url = reverse_lazy('mailing:subscribe_list')


class ClientListView(ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
