from django.test import TestCase
from rest_framework import status


class APISecureURLTestCase(TestCase):
    def test_secure_api_urls(self):
        secure_urls = [
            '/api/students/',
            '/api/applications/',
            '/api/flats/',
            '/api/residences/',
            '/api/users/',
        ]
        for url in secure_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
