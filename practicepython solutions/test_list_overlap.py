import unittest

from list_overlap import find_list_overlap

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


class Tests(unittest.TestCase):
    """Testing our functions."""

    def test_1(self):
        self.assertEqual(find_list_overlap(a, b), [1, 2, 3, 5, 8, 13])

    def test_2(self):
        self.assertEqual(find_list_overlap(c, d), [2, 4, 6, 8, 10])


if __name__ == "__main__":
    unittest.main()
