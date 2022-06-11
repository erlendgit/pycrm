import factory
from factory import post_generation

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)

    email = factory.Faker('email')

    @post_generation
    def post(user, create, extracted, **kwargs):
        kwargs.setdefault('password', 'secret')
        user.set_password(kwargs['password'])
