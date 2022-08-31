from django.core.management.base import BaseCommand
from crmapp.models import Lead, Status, Action, NextAction


class Command(BaseCommand):
    @staticmethod
    def add_status(self):
        status_context = ['Новый Лид', 'Авансировано', 'Проведена фотосессия', 'Фотографии отданы']
        with open('status.txt', 'w') as f:
            for status in status_context:
                f.write(status)
                print(f'записали в файл {status}')
        return

    def handle(self, *args, **options):
        leads = Lead.objects.all()
        print(leads)
        print(type(leads))
        for item in leads:
            print(item)
            print(type(item))
        print(f'Мы запустили скрипт {__name__}')

        add_status(self)
