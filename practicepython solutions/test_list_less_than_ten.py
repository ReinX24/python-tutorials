

import unittest

from list_less_than_ten import print_less_than_5

class Tests(unittest.TestCase):
    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 35, 55, 89]

    def test_1(self):
        self.assertEqual(print_less_than_5(self.a), [1, 1, 2, 3])

    def test_2(self):
        self.assertEqual(print_less_than_5(self.a), [1, 1, 2, 3])

    def test_3(self):
        self.assertEqual(print_less_than_5(self.a), [1, 1, 2, 3])

    def test_4(self):
        self.assertEqual(print_less_than_5(self.a), [1, 1, 2, 3])

    def test_5(self):
        self.assertEqual(print_less_than_5(self.a), [1, 1, 2, 3])
    
    def test_6(self):
        self.assertEqual(print_less_than_5(self.a), [1, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()