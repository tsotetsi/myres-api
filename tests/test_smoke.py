from django.test import TestCase


URLS_PUBLIC = [
    '/',
]


class SmokeTest(TestCase):
    def test_public_urls(self):
        for url in URLS_PUBLIC:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)
