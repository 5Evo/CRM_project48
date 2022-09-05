from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Lead
from .forms import ContactForm

# Create your views here.


def main_view(request):
    return render(request, 'crmapp/index.html', context={})


def leads_view(request):
    leads = Lead.objects.all()
    return render(request, 'crmapp/leads.html', context={'leads': leads})


def add_lead_view(request):
    if request.method == 'POST':            # если метод POST (передача данных через форму)
        form = ContactForm(request.POST, request.FILES)    # выводим форму с переданными в нее данными

        if form.is_valid():                 # если форма заполнена корретно

            # Получаем данные из формы:
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phoneNumber']
            second_phone_number = form.cleaned_data['secondPhoneNumber']
            mail = form.cleaned_data['mail']
            VK = form.cleaned_data['VK']
            TG = form.cleaned_data['TG']
            image = form.cleaned_data['image']
            # Получили

            # Создаем Лида из Формы:
            Lead.objects.create(first_name=first_name, middle_name = middle_name, last_name=last_name,
                                phoneNumber=phone_number, secondPhoneNumber=second_phone_number,
                                mail=mail, VK=VK, TG=TG, image=image)

            return HttpResponseRedirect(reverse('crm:leads'))       # После добавления Лида переходим в список всех лидов
        else:
             return render(request, 'crmapp/add_lead.html', context={'form': form})

    else:           # если метод GET (вывод новой формы)
        form = ContactForm()
        return render(request, 'crmapp/add_lead.html', context={'form': form})


def lead_card_view(request, id):
    lead = get_object_or_404(Lead, id=id)
    return render(request, 'crmapp/lead_card.html', context={'lead': lead})



def main_view_original(request):
    return render(request, 'crmapp/index_original.html', context={})


def charts_view(request):
    return render(request, 'crmapp/charts.html', context={})


def tables_view(request):
    return render(request, 'crmapp/tables.html', context={})


def buttons_view(request):
    return render(request, 'crmapp/buttons.html', context={})


def cards_view(request):
    return render(request, 'crmapp/cards.html', context={})


def blank_view(request):
    return render(request, 'crmapp/blank.html', context={})


def register_view(request):
    return render(request, 'crmapp/register.html', context={})


def utilities_color_view(request):
    return render(request, 'crmapp/utilities-color.html', context={})
