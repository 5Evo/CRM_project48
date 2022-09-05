'''
The module fill DB with test data form files.
All files (*.txt) are stored in the /project48/test_data folder
'''

from pathlib import Path
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from crmapp.models import Status, Action, Lead, Tag


class Command(BaseCommand):
    '''
    Standart class of DJANGO
    '''
    def handle(self, *args, **options):
        print(f'Мы запустили скрипт {__name__}')

        add_status()
        add_action()
        add_tags()
        add_leads()

def read_data(file):
    '''
    method for reading test_data from file
    :param file: file_name
    :return:
    '''
    dir_name = 'project48/test_data/'
    path_to_file = Path.cwd() / dir_name / file
    try:
        with open(path_to_file, 'r', encoding="utf-8") as test_file:
            result = test_file.read().split("\n")
    except FileNotFoundError as err:
        print(f'Не смогли прочитать файл {file}. Ошибка: {err}')
        result = []
    return result

def add_status():
    '''
    transferring 'status' from a file to a database
    :return:
    '''

    data_from_file = read_data('status.txt')
    for status in data_from_file:
        try:
            Status.objects.get(name=status)             # pylint: disable=E1101
            print(f'- Статус "{status}" уже есть в БД.')
        except ObjectDoesNotExist:
            Status.objects.create(name=status)          # pylint: disable=E1101
            print(f'Сохранили "{status}" в БД.')
    print('Записали Status в БД')


def add_action():
    '''
    transferring 'action' from a file to a database
    :return:
    '''
    data_from_file = read_data('action.txt')
    for action in data_from_file:
        try:
            Action.objects.get(name=action)             # pylint: disable=E1101
            print(f'- Действие "{action}" уже есть в БД.')
        except ObjectDoesNotExist:
            Action.objects.create(name=action)          # pylint: disable=E1101
            print(f'Сохранили "{action}" в БД.')
    print('Записали Action в БД')


def add_tags():
    '''
    transferring 'tags' from a file to a database
    :return:
    '''
    data_from_file = read_data('tags.txt')
    for tag in data_from_file:
        try:
            Tag.objects.get(name=tag)             # pylint: disable=E1101
            print(f'- Tag "{tag}" уже есть в БД.')
        except ObjectDoesNotExist:
            Tag.objects.create(name=tag)          # pylint: disable=E1101
            print(f'Сохранили "{tag}" в БД.')
    print('Записали Tags в БД')


def add_leads(quantity=30):
    '''
    random lead generation to db
    :return:
    '''
    for counter in range(quantity+1):
        try:
            Lead.objects.get(id=counter)  # pylint: disable=E1101
            print(f'- Lead "{counter}" уже есть в БД.')
        except ObjectDoesNotExist:
            first_name = f'Имя{counter}'
            last_name = f'Фамилия{counter}'
            phoneNumber = f'+01 {counter}  11 11'
            secondPhoneNumber = f'+02 {counter} 11 11'
            mail = f'{counter}@test.com'
            VK = f'VK_name_{counter}'
            TG = f'@tg_name_{counter}'
            Lead.objects.create(first_name = first_name, last_name = last_name,
                            phoneNumber = phoneNumber, secondPhoneNumber = secondPhoneNumber,
                            mail = mail, VK = VK, TG = TG)
            print(f'Сохранили "lead{counter}" в БД.')
    print('Записали Leads в БД')