from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

from .forms import RegistrationForm, LoginForm
from django.views.generic import CreateView
from .models import CrmUser

# Create your views here.


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    authentication_form = LoginForm


class UserCreateView(CreateView):
    model = CrmUser
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')

