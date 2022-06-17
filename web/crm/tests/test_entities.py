import faker
from django.test import TestCase

from crm.factories import EntityFactory


class TestEntitiesTestCase(TestCase):

    def test_create_form_creates_entity(self):
        from crm.forms import EntityUpdateForm
        values = {
            'name': faker.Faker().name(),
            'pitch': faker.Faker().sentence(),
        }
        form = EntityUpdateForm(values)
        entity = form.create()

        self.assertIsNotNone(entity.id)
        self.assertEqual(entity.name, values['name'])
        self.assertEqual(entity.pitch, values['pitch'])

    def test_update_form_updates_entity(self):
        from crm.forms import EntityUpdateForm
        entity = EntityFactory()
        values = {
            'name': faker.Faker().name(),
            'pitch': faker.Faker().sentence(),
        }
        form = EntityUpdateForm(values, entity=entity)
        saved_entity = form.update()

        self.assertEqual(saved_entity.id, entity.id)
        self.assertEqual(saved_entity.name, values['name'])
        self.assertEqual(saved_entity.pitch, values['pitch'])

    def test_update_form_requires_entity(self):
        from crm.forms import EntityUpdateForm
        values = {
            'name': faker.Faker().name(),
            'pitch': faker.Faker().sentence(),
        }
        with self.assertRaises(AttributeError):
            form = EntityUpdateForm(values)
            form.update()
