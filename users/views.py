import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from users.forms import UserRegisterForm, UserManagerForm
from users.models import User

from django.conf import settings
from django.core.mail import send_mail


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        token = secrets.token_hex(16)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f'http://{host}/users/confirm-register/{token}'
        message = f'Вы успешно зарегистрировались, для доступа подтвердите регистрацию по ссылке: {link}'
        send_mail('Верификация почты', message, settings.EMAIL_HOST_USER, [user.email])
        return super().form_valid(form)


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserManagerView(LoginRequiredMixin, ListView):
    model = User


class UserManagerUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserManagerForm
    success_url = reverse_lazy('users:user_list')
