"""
Simple tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(2, 6)

        self.assertEqual(res, 8)

    def text_subtract_numbers(self):
        """Text subtrating numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
