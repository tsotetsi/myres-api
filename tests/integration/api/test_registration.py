from django.core import mail

from rest_framework.test import APITestCase
from rest_framework import status

from tests import factories


class RegistrationTestCase(APITestCase):
    url = 'http://localhost:8000/api/rest-auth/registration/'

    def test_registration(self):
        residence = factories.ResidenceFactory()
        data = {
            'residence': residence.id,
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

    def test_registration_with_invalid_password(self):
        # registering with invalid password should raise an error.
        pass

    def test_registration_with_invalid_mobile_number(self):
        # registering with invalid mobile number should raise an error.
        pass

    def test_registration_with_invalid_gender_choice(self):
        # registering with invalid gender choice should raise an error.
        pass

    def test_registration_activation_token_link(self):
        pass
