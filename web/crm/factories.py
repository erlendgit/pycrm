import factory

from crm.models import Entity, Reference


class EntityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entity
        django_get_or_create = ('name',)

    name = factory.Faker('name')
    pitch = factory.Faker('sentence')


class ReferenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reference

    entity = factory.SubFactory(EntityFactory)
    reference = factory.SubFactory(EntityFactory)
    relation_type = factory.Faker('sentence')