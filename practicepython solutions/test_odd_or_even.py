import unittest

from odd_or_even import check_odd_or_even, check_divides_evenly

class Tests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(check_odd_or_even(3),"Odd")

    def test_2(self):
        self.assertEqual(check_odd_or_even(5),"Odd")

    def test_3(self):
        self.assertEqual(check_odd_or_even(7),"Odd")

    def test_4(self):
        self.assertEqual(check_odd_or_even(2),"Even")

    def test_5(self):
        self.assertEqual(check_odd_or_even(10),"Even")
    
    def test_6(self):
        self.assertEqual(check_odd_or_even(14),"Even")

    def test_7(self):
        self.assertEqual(check_odd_or_even(4),"Multiple of 4")

    def test_8(self):
        self.assertEqual(check_odd_or_even(8),"Multiple of 4")
    
    def test_9(self):
        self.assertEqual(check_odd_or_even(12),"Multiple of 4")
        
    def test_10(self):
        self.assertEqual(check_divides_evenly(4, 2),"4 divides evenly by 2")

    def test_11(self):
        self.assertEqual(check_divides_evenly(6, 3),"6 divides evenly by 3")
    
    def test_12(self):
        self.assertEqual(check_divides_evenly(5, 3),"5 does not divide evenly by 3")

if __name__ == '__main__':
    unittest.main()