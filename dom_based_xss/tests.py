from django.test import TestCase

from django.contrib.auth.models import User
from dom_based_xss.models import Text
from website.models import DomBasedXssModule
# Create your tests here.


class TextTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username='testUser', password='testPassword')
        test_module = DomBasedXssModule.objects.create(user=test_user)
        Text.objects.create(text='Test Text', dom_based_xss_module_related=test_module)


    def test_Text_str_dunder(self):
        '''tests if __str__ dunder method works correctly'''

        test_user = User.objects.get(username='testUser')
        test_module = DomBasedXssModule.objects.get(user=test_user)
        test_text = Text.objects.get(text='Test Text')
        self.assertEqual(test_text.__str__(), 'Test Text')
