import unittest
from django_proxy_model_problems.models import MyProxyUser


class InheritingFromUnittestTestCase(unittest.TestCase):

    def test_empty_db(self):
        self.assertEqual(0, MyProxyUser.objects.count())
