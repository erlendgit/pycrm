from django.test import TestCase
from django.urls import reverse


class TestHomepageTestCase(TestCase):

    def test_homepage(self):
        result = self.client.get(reverse('core:home'))
        self.assertEqual(result.status_code, 200)
