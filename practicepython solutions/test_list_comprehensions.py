import unittest

from list_comprehesions import eval_even_list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in range(1, 11)]


class Tests(unittest.TestCase):
    """Test a function that returns a list with only even elements."""

    def test_1(self):
        self.assertEqual(eval_even_list(a), [4, 16, 36, 64, 100])

    def test_2(self):
        self.assertEqual(eval_even_list(b), [2, 4, 6, 8, 10])


if __name__ == "__main__":
    unittest.main()
