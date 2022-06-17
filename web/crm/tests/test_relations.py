import faker
from django.test import TestCase

from crm.factories import EntityFactory, ReferenceFactory
from crm.forms import EntityRelationForm
from crm.models import Reference


class TestRelationsTestCase(TestCase):

    def setUp(self) -> None:
        super(TestRelationsTestCase, self).setUp()
        self.entity = EntityFactory(name="Entity")
        self.other = EntityFactory(name="Other")

    def test_form_prevents_to_relate_to_self(self):
        form = EntityRelationForm({
            'reference': self.entity.id,
            'relation_type': 'For testing',
        }, entity=self.entity)

        self.assertFalse(form.is_valid())

    def test_form_prevents_to_create_duplicates(self):
        ReferenceFactory(entity=self.entity, reference=self.other)

        form = EntityRelationForm({
            'reference': self.other.id,
            'relation_type': 'For testing',
        }, entity=self.entity)

        self.assertFalse(form.is_valid())

    def test_form_properly_used_results_in_a_reference(self):
        RELATION_TYPE = faker.Faker().sentence()
        form = EntityRelationForm({
            'reference': self.other.id,
            'relation_type': RELATION_TYPE,
        }, entity=self.entity)

        form.is_valid()
        reference = form.save()

        assert reference.id
        assert reference.entity.id == self.entity.id
        assert reference.reference.id == self.other.id
        assert reference.relation_type == RELATION_TYPE

    def test_relations_for(self):
        third = EntityFactory(name="Gamma")
        fourth = EntityFactory(name="Alpha")

        ReferenceFactory(entity=self.entity,
                         reference=self.other)
        ReferenceFactory(entity=self.entity,
                         reference=third)
        ReferenceFactory(entity=self.entity,
                         reference=fourth)

        entity_references = Reference.objects.collect_for(self.other)
        self.assertEqual(1, len(entity_references), msg="Error at %s" % self.other)

        entity_references = Reference.objects.collect_for(self.entity)
        self.assertEqual(3, len(entity_references), msg="Error at %s" % self.entity)

        names = [r[1].name for r in entity_references]
        self.assertEqual(names, ['Alpha', 'Gamma', 'Other'])
