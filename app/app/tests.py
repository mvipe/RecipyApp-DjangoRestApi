from django.test import TestCase

from .calc import add,subctract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two number add together"""
        self.assertEqual(add(3,8),11)
        self.assertEqual(add(83, 8), 91)

    def test_substract_numbers(self):
        """Test that two number add together"""
        self.assertEqual(subctract(8,3),5)
