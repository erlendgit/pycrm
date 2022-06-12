import factory

from crm.models import Entity


class EntityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entity
        django_get_or_create = ('name',)

    name = factory.Faker('name')
    pitch = factory.Faker('sentence')
