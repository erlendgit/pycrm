from django.test import TestCase

from core.lib import filter_html


class TestHtmlInputTestCase(TestCase):

    def test_input_with_class_attributes(self):
        value = """
                <div class="keep-class" data-to-loose="lose-data">
                    content
                </div>
                """
        self.assertIn('keep-class', filter_html(value))
        self.assertNotIn('lose-data', filter_html(value))
