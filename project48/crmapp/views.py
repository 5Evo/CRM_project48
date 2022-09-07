from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Lead
from .forms import CreateForm


def main_view(request):
    return render(request, 'crmapp/index.html', context={})


class LeadListView(ListView):
    model = Lead
    template_name = 'crmapp/lead_list.html'


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'crmapp/lead_card.html'


class LeadCreateView(CreateView):
    form_class = CreateForm
    model = Lead
    success_url = reverse_lazy('crm:leads')
    template_name = 'crmapp/create_lead.html'

class LeadUpdateView(UpdateView):
    form_class = CreateForm
    model = Lead
    success_url = reverse_lazy('crm:leads')
    template_name = 'crmapp/update_lead.html'


class LeadDeleteView(DeleteView):
    model = Lead
    success_url = reverse_lazy('crm:leads')
    template_name = 'crmapp/lead_delete_confirm.html'


# Нижеследующие вьюшки не переведены на cbv, тк не используются в проекте и оставлены пока для примера возможностей Bootstrap

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
