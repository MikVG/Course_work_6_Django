from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, confirm_email, UserManagerView, UserManagerUpdate

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-register/<str:token>', confirm_email, name='confirm_email'),
    path('user-list', UserManagerView.as_view(), name='user_list'),
    path('user-update/<int:pk>/', UserManagerUpdate.as_view(), name='user-update'),
]
