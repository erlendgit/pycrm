from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from crm.factories import EntityFactory
from user.factories import UserFactory


class TestPathsTestCase(TestCase):

    def setUp(self):
        super(TestPathsTestCase, self).setUp()
        self.user = UserFactory()
        self.entity = EntityFactory()

    def test_index_path(self):
        self.assertEqual('/crm/', reverse("crm:index"))

    def test_index_content(self):
        user = UserFactory()
        entity = EntityFactory()
        self.client.force_login(user)

        response: HttpResponse = self.client.get(reverse("crm:index"))

        self.assertIn(entity.url, response.content.decode())
        self.assertIn(entity.name, response.content.decode())

    def test_view_path(self):
        self.assertEqual(f'/crm/{self.entity.id}/', self.entity.url)

    def test_view_content(self):
        user = UserFactory()
        entity = EntityFactory()
        self.client.force_login(user)

        response: HttpResponse = self.client.get(reverse("crm:index"))
