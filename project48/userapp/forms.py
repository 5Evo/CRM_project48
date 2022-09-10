from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CrmUser


class RegistrationForm(UserCreationForm):

    username = forms.CharField(label='ИМЯ', widget=forms.TextInput(attrs={'placeholder': 'ИМЯ', 'class': 'form-control'}))
    email = forms.EmailField(label='EMAIL', required=False, widget=forms.EmailInput(attrs={'placeholder': 'email', 'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'пароль', 'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'повторите пароль', 'class': 'form-control'}))
    avatar = forms.ImageField(label='Аватарка', required=False)

    class Meta:
        model = CrmUser
        fields = ('username', 'password1', 'password2', 'email', 'avatar')


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='ИМЯ', widget=forms.TextInput(attrs={'placeholder': 'Ваше ИМЯ', 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'}))
