from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Lead
from .forms import CreateForm, UserChangeForm


def main_view(request):
    return render(request, 'crmapp/index.html', context={})


class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    # Django 4.1 does not require to specify a template if name is '{object}_list.html':
    # template_name = 'crmapp/lead_list.html'

    def get_queryset(self):
        """
        Getting a list of leads for the current user
        :return:
        """
        # get_by_user - custom method from UserQuerySet.get_by_user():
        return super().get_queryset().get_by_user(self.request)

        # for older version Django where 'user=self.request.user' - current (logged in) user:
        # return Lead.objects.filter(user=self.request.user)


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'crmapp/lead_card.html'


class LeadCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateForm
    #form_class = UserChangeForm
    model = Lead
    success_url = reverse_lazy('crm:leads')
    template_name = 'crmapp/create_lead.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел POST запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        '''
        Метод срабатывает после того, как форма валидна
        :param form:
        :return:
        '''
        # self.request.user - текущий пользователь
        # Передадим в текущую форму (form.instance) создания Лида юзера, который заполняет форму
        # другими словами укажем в качестве владельца Лида текущего пользователя:
        form.instance.user = self.request.user
        return super().form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CreateForm
    model = Lead
    success_url = reverse_lazy('crm:leads')
    template_name = 'crmapp/update_lead.html'


class LeadDeleteView(LoginRequiredMixin, DeleteView):
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
