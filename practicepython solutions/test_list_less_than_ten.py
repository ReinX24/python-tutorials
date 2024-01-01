import unittest

from list_less_than_ten import less_than_5, less_than_num


class Tests(unittest.TestCase):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 35, 55, 89]

    def test_1(self):
        self.assertEqual(less_than_5(self.a), [1, 1, 2, 3])

    def test_2(self):
        self.assertEqual(less_than_5(self.a), [1, 1, 2, 3])

    def test_3(self):
        self.assertEqual(less_than_5(self.a), [1, 1, 2, 3])

    def test_4(self):
        self.assertEqual(less_than_5(self.a), [1, 1, 2, 3])

    def test_5(self):
        self.assertEqual(less_than_5(self.a), [1, 1, 2, 3])

    def test_6(self):
        self.assertEqual(less_than_5(self.a), [1, 1, 2, 3])

    def test_7(self):
        self.assertEqual(less_than_num(self.a, 3), [1, 1, 2])

    def test_8(self):
        self.assertEqual(less_than_num(self.a, 7), [1, 1, 2, 3, 5])

    def test_9(self):
        self.assertEqual(less_than_num(self.a, 10), [1, 1, 2, 3, 5, 8])


if __name__ == "__main__":
    unittest.main()
