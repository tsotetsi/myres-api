from django.test import TestCase
from rest_framework import status


URLS_API = [
    '/api/students/',
    '/api/applications/',
    '/api/flats/',
    '/api/residences/',
    '/api/users/',
]


class APIURLSecureTestCase(TestCase):
    def test_secure_api_urls(self):
        for url in URLS_API:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
