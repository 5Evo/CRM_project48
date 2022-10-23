from django.test import Client, TestCase
from mixer.backend.django import mixer
from crmapp.models import Lead
from userapp.models import CrmUser


class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    # Проверим страницы, не требующие авторизации:
    def test_statuses(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/index/')
        self.assertEqual(responce.status_code, 200)

    # без логина пользователя - редирект на авторизацию (ответ 302)
    def test_login_required(self):

        CrmUser.objects.create_user(username='admin', password='admin123')
        # user не залогинен:
        responce = self.client.get('/lead_list/')
        self.assertEqual(responce.status_code, 302)

        responce = self.client.get('/lead_card/1/')
        self.assertEqual(responce.status_code, 302)

        responce = self.client.get('/create_lead/')
        self.assertEqual(responce.status_code, 302)

        responce = self.client.get('/lead_update/1/')
        self.assertEqual(responce.status_code, 302)

        responce = self.client.get('/lead_delete/1/')
        self.assertEqual(responce.status_code, 302)

        self.client.login(username='admin', password='admin123')    # залогинили пользователя
        lead = mixer.blend(Lead)    # создали Лида под пользователем

        print(f'тестируем созданного лида {lead.id}: {lead}')
        print(f'Имя пользователя: {self.client.username}')

        # после логина все ответы должны быть '200':
        responce = self.client.get('/lead_list/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/lead_card/1/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/create_lead/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/lead_update/1/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/lead_delete/1/')
        self.assertEqual(responce.status_code, 200)
