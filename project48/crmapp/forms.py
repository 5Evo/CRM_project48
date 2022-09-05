from django import forms

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