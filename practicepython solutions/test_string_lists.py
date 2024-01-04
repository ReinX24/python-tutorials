import unittest

from string_lists import is_palindrome


class Tests(unittest.TestCase):
    """Testing our is_palindrome function."""

    def test_1(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_2(self):
        self.assertFalse(is_palindrome("rein"))

    def test_3(self):
        self.assertTrue(is_palindrome("civic"))

    def test_4(self):
        self.assertFalse(is_palindrome("rain"))


if __name__ == "__main__":
    unittest.main()
