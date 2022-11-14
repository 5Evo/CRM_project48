from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget, PhoneNumberPrefixWidget
from .models import Lead, Tag

# ContactForm is not used (temporarily)
# class ContactForm(forms.Form):
#
#     first_name = forms.CharField(label='ИМЯ (обязательно)')
#     middle_name = forms.CharField(label='Отчество', required=False)
#     last_name = forms.CharField(label='ФАМИЛИЯ', required=False)
#     phoneNumber = forms.CharField(label='ТЕЛЕФОН', required=False)
#     secondPhoneNumber = forms.CharField(label='ТЕЛЕФОН', required=False)
#     mail = forms.EmailField(label='EMAIL', required=False)
#     VK = forms.CharField(label='VK', required=False)
#     TG = forms.CharField(label='TG', required=False)
#     image = forms.ImageField(label='ФОТО', required=False)


# Форма для создания нового Лида
class CreateForm(forms.ModelForm):
    class Meta:
        model = Lead
        exclude = ('user',)

    first_name = forms.CharField(label='ИМЯ (обязательно)', widget=forms.TextInput(attrs={'placeholder': 'ИМЯ (обязательно)', 'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', required=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'form-control'}))
    last_name = forms.CharField(label='ФАМИЛИЯ (обязательно)', widget=forms.TextInput(attrs={'placeholder': 'ФАМИЛИЯ (обязательно)', 'class': 'form-control'}))
    phoneNumber = PhoneNumberField(label='ТЕЛЕФОН', required=False, widget=RegionalPhoneNumberWidget(attrs={'placeholder': '+7 XXX XXX XX XX', 'class': 'form-control'}))
    phoneNumber.error_messages['invalid'] = 'Неправльный формат телефона!'
    mail = forms.EmailField(label='EMAIL', required=False, widget=forms.EmailInput(attrs={'placeholder': 'email', 'class': 'form-control'}))
    VK = forms.CharField(label='VK', required=False, widget=forms.TextInput(attrs={'placeholder': 'VK', 'class': 'form-control'}))
    TG = forms.CharField(label='TG', required=False, widget=forms.TextInput(attrs={'placeholder': 'TG', 'class': 'form-control'}))
    image = forms.ImageField(label='ФОТО', required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name', 'phoneNumber')

    first_name = forms.CharField(label='ИМЯ (обязательно)', widget=forms.TextInput(
        attrs={'placeholder': 'ИМЯ (обязательно)', 'class': 'form-control'}))
    phoneNumber = PhoneNumberField(label='ТЕЛЕФОН', required=False, widget=RegionalPhoneNumberWidget(
        attrs={'placeholder': 'ТЕЛЕФОН', 'class': 'form-control'}))
    #phoneNumber = PhoneNumberField(label='ТЕЛЕФОН', widget=RegionalPhoneNumberWidget(initial='RU', attrs={'placeholder': '+79001112233', 'class': 'form-control'}))
    phoneNumber.error_messages['invalid'] = 'Неправильный номер телефона!'

