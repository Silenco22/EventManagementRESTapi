from django.test.client import Client
from django.test import TestCase
import json
from django.urls import reverse
from api.views import createUser
from account.models import Account
from event.models import Meeting
# class TestCase(SimpleTestCase):
#   def test_myview(self):
#     c = Client()
#     response = c.get(reverse('my_view'))


# 'email', 'username', 'password', 'password2'

class UserCreationTesting(TestCase):
    def test_createUser(self):
        payload = {"email": "j@j.com", "username": "jay","password": 'dado1234',"password2":'dado1234'}

        Header = {'HTTP_AUTHORIZATION': 'auth_token'}
        response = Client().post(reverse('create_User'), data=json.dumps(payload),  content_type ='application/json')
        user = Account.objects.filter(username="jay")
        print(user)
        self.assertIsNotNone(user)

class MeetingCreationTesting(TestCase):
    def test_createMeeting(self):

        payload1 = {"email": "j@j.com", "username": "jay","password": 'dado1234',"password2":'dado1234'}
        payload2 = {"creator": "1", "event_name": "Event"}
        payload3 = {"user": "1", "event_name": "Event"}
        payload4 = {"user": "1", "meeting_name": "Meeting1","event_name": '1',"meeting_date":'2022-03-17',"array":'1'}

        Header = {'HTTP_AUTHORIZATION': 'auth_token'}
        
        response1 = Client().post(reverse('create_User'), data=json.dumps(payload1),  content_type ='application/json')
        response2 = Client().post(reverse('create_Event'), data=json.dumps(payload2),  content_type ='application/json')
        response3 = Client().post(reverse('add_participant'), data=json.dumps(payload3),  content_type ='application/json')
        response4 = Client().post(reverse('create_meeting'), data=json.dumps(payload4),  content_type ='application/json')
        user = Meeting.objects.filter(meeting_name="Meeting1")
        print(user)
        self.assertIsNotNone(user)
