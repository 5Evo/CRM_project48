from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render

from crmapp.models import UserDataMixin
from . import models
from .forms import LoginForm, CustomUserCreationForm
from django.views.generic import CreateView, DetailView
from .models import CrmUser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    authentication_form = LoginForm


class UserCreateView(CreateView):
    model = CrmUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('userapp:login')
    template_name = 'userapp/register.html'


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CrmUser
    print(f'Профиль пользователя: {CrmUser}')
    success_url = reverse_lazy('userapp:profile')
    template_name = 'userapp/profile.html'


def update_token_ajax(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else:
        # создать
        token = Token.objects.create(user=user)
    return JsonResponse({'key': token.key})


def forgot_password_view(request):
    return render(request, 'userapp/forgot-password.html', context={})