from django.test import TestCase
from django.urls import reverse

from crm.factories import EntityFactory


class TestPathsTestCase(TestCase):
    def test_index_path(self):
        self.assertEqual('/crm/', reverse("crm:index"))

    def test_view_path(self):
        entity = EntityFactory()
        self.assertEqual(f'/crm/{entity.id}/', reverse('crm:view', args=(entity.id,)))