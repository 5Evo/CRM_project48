from django import forms
from .models import Lead, Tag

class ContactForm(forms.Form):

    first_name = forms.CharField(label='ИМЯ (обязательно)')
    middle_name = forms.CharField(label='Отчество', required=False)
    last_name = forms.CharField(label='ФАМИЛИЯ', required=False)
    phoneNumber = forms.CharField(label='ТЕЛЕФОН', required=False)
    secondPhoneNumber = forms.CharField(label='ТЕЛЕФОН', required=False)
    mail = forms.EmailField(label='EMAIL', required=False)
    VK = forms.CharField(label='VK', required=False)
    TG = forms.CharField(label='TG', required=False)
    image = forms.ImageField(label='ФОТО', required=False)

class CreateForm(forms.ModelForm):
    first_name = forms.CharField(label='ИМЯ (обязательно)', widget=forms.TextInput(attrs={'placeholder': 'ИМЯ (обязательно)', 'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', required=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'form-control'}))
    last_name = forms.CharField(label='ФАМИЛИЯ', required=False, widget=forms.TextInput(attrs={'placeholder': 'ФАМИЛИЯ', 'class': 'form-control'}))
    phoneNumber = forms.CharField(label='ТЕЛЕФОН', required=False, widget=forms.TextInput(attrs={'placeholder': 'ТЕЛЕФОН', 'class': 'form-control'}))
    secondPhoneNumber = forms.CharField(label='ТЕЛЕФОН', required=False, widget=forms.TextInput(attrs={'placeholder': 'ВТОРОЙ ТЕЛЕФОН', 'class': 'form-control'}))
    mail = forms.EmailField(label='EMAIL', required=False, widget=forms.TextInput(attrs={'placeholder': 'EMAIL', 'class': 'form-control'}))
    VK = forms.CharField(label='VK', required=False, widget=forms.TextInput(attrs={'placeholder': 'VK', 'class': 'form-control'}))
    TG = forms.CharField(label='TG', required=False, widget=forms.TextInput(attrs={'placeholder': 'TG', 'class': 'form-control'}))
    image = forms.ImageField(label='ФОТО', required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Lead
        fields = '__all__'

