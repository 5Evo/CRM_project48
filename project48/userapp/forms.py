from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import CrmUser


#Форма, котрая работает по умолчанию
# class RegistrationForm(UserCreationForm):
#
#     username = forms.CharField(label='ИМЯ', widget=forms.TextInput(attrs={'placeholder': 'ИМЯ', 'class': 'form-control'}))
#     email = forms.EmailField(label='EMAIL', required=False, widget=forms.EmailInput(attrs={'placeholder': 'email', 'class': 'form-control'}))
#     password1 = forms.CharField(label='Пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'пароль', 'class': 'form-control'}))
#     password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'повторите пароль', 'class': 'form-control'}))
#     avatar = forms.ImageField(label='Аватарка', required=False)
#
#     class Meta:
#         model = CrmUser
#         fields = ('username', 'password1', 'password2', 'email', 'avatar')


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='ИМЯ', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(label='Аватарка (по желанию)', required=False)
    class Meta:
        model = CrmUser
        fields = ('username', 'password1', 'password2', 'email', 'avatar')

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = CrmUser.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = CrmUser.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = CrmUser.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password1']
                )
        return user


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='ИМЯ', widget=forms.TextInput(attrs={'placeholder': 'Ваше ИМЯ', 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'}))
