from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from core.menu import MENU
from user.factories import UserFactory


class TestMenuTestCase(TestCase):

    def test_main_menu_anonymous_menu_items(self):
        request = HttpRequest()
        request.user = AnonymousUser()

        menu = MENU['main']

        self.assertEqual([i.url for i in menu.get_children(request)],
                         [reverse('core:home'),
                          reverse('core:date_convert')])

    def test_main_menu_authorized_user(self):
        request = HttpRequest()
        request.user = UserFactory()

        menu = MENU['main']

        self.assertEqual([i.url for i in menu.get_children(request)],
                         [reverse('core:home'),
                          reverse('core:date_convert'),
                          reverse('crm:index')])
