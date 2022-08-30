from django.core.management.base import BaseCommand
from crmapp.models import Lead, Status, Action, NextAction


# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):
        leads = Lead.objects.all()
        print(leads)
        print(type(leads))
        for item in leads:
            print(item)
            print(type(item))
        print(f'Мы запустили скрипт {__name__}')