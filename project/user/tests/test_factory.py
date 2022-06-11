from django.test import TestCase

from user.factories import UserFactory


class TestFactoryTestCase(TestCase):

    def test_factory_works(self):
        user = UserFactory()
        self.assertFalse(user.check_password("known-false"))
        self.assertTrue(user.check_password('secret'))