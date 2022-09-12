from django.test import TestCase
from mixer.backend.django import mixer
from .models import Lead, Tag, Status, Action, NextAction


# Tests of Models
class LeadTestCaseMixer(TestCase):
    def setUp(self):
        self.lead = mixer.blend(Lead, first_name='Alex', middle_name='Leo', last_name='Thomson')

    def test_lead_has_image(self):
        self.assertFalse(self.lead.has_image())

    def test_lead_str(self):
        self.assertEqual(str(self.lead), 'Alex Leo Thomson')

class TagTestCaseMixer(TestCase):
    def setUp(self):
        self.tag=mixer.blend(Tag, name='tag1')

    def test_tag_str(self):
        self.assertEqual(str(self.tag), 'tag1')


class StatusTestCaseMixer(TestCase):
    def setUp(self):
        self.status = mixer.blend(Status, name='OK')

    def test_status_str(self):
        self.assertEqual(str(self.status), 'OK')


class ActionTestCaseMixer(TestCase):
    def setUp(self):
        self.action = mixer.blend(Action, name='next')

    def test_action_str(self):
        self.assertEqual(str(self.action), 'next')


class NextActionTestCaseMixer(TestCase):
    def setUp(self):
        self.next_action = mixer.blend(NextAction, lead__first_name='Alex', lead__middle_name='Leo', lead__last_name='Thomson', action_type__name='call', action_date='2022-09-23' )

    def test_next_action_str(self):
        self.assertEqual(str(self.next_action), 'Alex Leo Thomson - call 2022-09-23')
