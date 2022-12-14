from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import LoginForm, CustomUserCreationForm
from django.views.generic import CreateView
from .models import CrmUser


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'
    authentication_form = LoginForm


class UserCreateView(CreateView):
    model = CrmUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login')
    template_name = 'userapp/register.html'
