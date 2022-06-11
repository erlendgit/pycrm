from django.test import TestCase
from django.urls import reverse


class TestPathsTestCase(TestCase):
    def test_login_url(self):
        self.assertEqual(reverse('user:login'), '/user/login/')