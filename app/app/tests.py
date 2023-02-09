from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the Calc module"""
    def test_add_numbers(self):
        """Add numbers testing"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Subtract numbers testing"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
