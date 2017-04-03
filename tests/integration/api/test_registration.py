from django.core import mail

from rest_framework.test import APITestCase
from rest_framework import status


class RegistrationTestCase(APITestCase):
    url = 'http://localhost:8000/api/rest-auth/registration/'

    def test_registration(self):
        data = {
            'name': 'John',
            'surname': 'Doe',
            'mobile_number': '+27835504933',
            'email': 'john.does@myuniversity.ac.za',
            'gender': 'MALE',
            'password1': 'pass1@Capital',
            'password2': 'pass1@Capital'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test that an activation get sent to student
        self.assertEqual(len(mail.outbox), 1)
