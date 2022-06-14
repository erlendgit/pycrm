from django.http import HttpRequest
from django.test import TestCase

from core.menu import MENU
from user.factories import UserFactory


class TestMenuTestCase(TestCase):

    def test_main_menu_anonymous_menu_items(self):
        request = HttpRequest()
        request.user = UserFactory()

        menu = MENU['main']

        for item in menu.get_children(request):
            self.fail(item)
