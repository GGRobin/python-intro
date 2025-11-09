# test_app.py
import unittest
from app import (
    is_valid_email,
    calculate_circle_area,
    filter_even_numbers,
    convert_date_format,
    is_palindrome,
)

class TestApp(unittest.TestCase):

    # ---------- is_valid_email ----------
    def test_is_valid_email_typical(self):
        self.assertTrue(is_valid_email("user@example.com"))

    def test_is_valid_email_no_at(self):
        self.assertFalse(is_valid_email("userexample.com"))

    def test_is_valid_email_no_dot_after_at(self):
        self.assertFalse(is_valid_email("user@examplecom"))

    # ---------- calculate_circle_area ----------
    def test_calculate_circle_area_typical(self):
        area = calculate_circle_area(1)
        # pole kola r=1 powinno byc bliskie pi
        self.assertAlmostEqual(area, 3.14159, places=4)

    def test_calculate_circle_area_zero(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_calculate_circle_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-2)

    # ---------- filter_even_numbers ----------
    def test_filter_even_numbers_typical(self):
        self.assertEqual(filter_even_numbers([1,2,3,4,0,-2]), [2,4,0,-2])

    def test_filter_even_numbers_empty(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_filter_even_numbers_non_int(self):
        self.assertEqual(filter_even_numbers([1,2,"3",4.0]), [2])

    # ---------- convert_date_format ----------
    def test_convert_date_format_typical(self):
        self.assertEqual(convert_date_format("2025-11-09"), "09/11/2025")

    def test_convert_date_format_bad(self):
        with self.assertRaises(ValueError):
            convert_date_format("09-11-2025")

    def test_convert_date_format_edge(self):
        self.assertEqual(convert_date_format("0001-01-01"), "01/01/0001")

    # ---------- is_palindrome ----------
    def test_is_palindrome_simple(self):
        self.assertTrue(is_palindrome("Kobyla ma maly bok"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("To nie jest"))

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()
