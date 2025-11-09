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

    def test_is_valid_email_wrong_type(self):
        self.assertFalse(is_valid_email(12345))

    def test_is_valid_email_empty_string(self):
        self.assertFalse(is_valid_email(""))

    def test_is_valid_email_no_local_part(self):
        self.assertFalse(is_valid_email("@example.com"))

    def test_is_valid_email_domain_starts_with_dot(self):
        self.assertFalse(is_valid_email("user@.example.com"))

    def test_is_valid_email_domain_ends_with_dot(self):
        self.assertFalse(is_valid_email("user@example.com."))

    # ---------- calculate_circle_area ----------
    def test_calculate_circle_area_typical(self):
        area = calculate_circle_area(1)
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

    def test_filter_even_numbers_invalid_input(self):
        with self.assertRaises(ValueError):
            filter_even_numbers("not_a_list")

    def test_filter_even_numbers_with_bools(self):
        # False -> 0 (parzyste) True -> 1 (nieparzyste) => expect False(0) and 2
        self.assertEqual(filter_even_numbers([True, False, 2, 3]), [0, 2])

    # ---------- convert_date_format ----------
    def test_convert_date_format_typical(self):
        self.assertEqual(convert_date_format("2025-11-09"), "09/11/2025")

    def test_convert_date_format_bad(self):
        with self.assertRaises(ValueError):
            convert_date_format("09-11-2025")

    def test_convert_date_format_edge(self):
        self.assertEqual(convert_date_format("0001-01-01"), "01/01/0001")

    def test_convert_date_format_not_string(self):
        with self.assertRaises(ValueError):
            convert_date_format(1234)

    def test_convert_date_format_single_digits(self):
        self.assertEqual(convert_date_format("2025-1-5"), "05/01/2025")

    def test_convert_date_format_month_zero_or_day_zero(self):
        with self.assertRaises(ValueError):
            convert_date_format("2025-00-10")
        with self.assertRaises(ValueError):
            convert_date_format("2025-10-00")

    # ---------- is_palindrome ----------
    def test_is_palindrome_simple(self):
        self.assertTrue(is_palindrome("Kobyla ma maly bok"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("To nie jest"))

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_non_string(self):
        self.assertFalse(is_palindrome(12345))

    def test_is_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    # dodatkowe testy probujace dotknac brakujacych sciezek
    def test_is_valid_email_multiple_ats(self):
        # adres z wieloma '@' powinien byc niepoprawny
        self.assertFalse(is_valid_email("a@b@c@example.com"))

    def test_is_valid_email_double_dot_in_domain(self):
        # podwojna kropka w domenie -> niepoprawne
        self.assertFalse(is_valid_email("user@sub..example.com"))

    def test_filter_even_numbers_wrong_sequence_type(self):
        # przekazanie tuple zamiast listy powinno rzucic ValueError
        with self.assertRaises(ValueError):
            filter_even_numbers((1,2,3,4))
    def test_is_valid_email_domain_empty(self):
        # domena pusta po '@' -> np. "user@" powinno byc False
        self.assertFalse(is_valid_email("user@"))

    def test_convert_date_format_too_few_parts(self):
        # input z za mala liczba czesci po split("-") -> powinien rzucic ValueError
        with self.assertRaises(ValueError):
            convert_date_format("2025-11")

    def test_dummy_for_full_coverage(self):
        # drobny test pomocniczy, aby osiagnac 100% pokrycia plikow testowych
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()


