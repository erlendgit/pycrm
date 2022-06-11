from django.test import TestCase

from crm.factories import EntityFactory
from crm.models import Entity


class TestFactoryTestCase(TestCase):

    def test_factory_works(self):
        entity = EntityFactory()
        self.assertIsNotNone(entity.name)
        self.assertIsNotNone(entity.pitch)

        self.assertEqual(1, Entity.objects.all().count())

    def test_factory_generates_more_then_one(self):
        EntityFactory()
        EntityFactory()
        self.assertEqual(2, Entity.objects.all().count())

    def test_factory_generates_one_of_a_name(self):
        reference = EntityFactory()
        EntityFactory(name=reference.name)
        self.assertEqual(1, Entity.objects.all().count())
