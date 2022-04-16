from django.test import TestCase

from .calc import add


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two number add together"""
        self.assertEqual(add(3,8),11)
        self.assertEqual(add(83, 8), 11)