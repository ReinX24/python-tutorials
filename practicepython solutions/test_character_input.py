import unittest

from character_input import tell_when__100_years_old, repeat_message

class Tests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(tell_when__100_years_old('rein', 20), 'Rein will be 100 at 2103.')

    def test_2(self):
        self.assertEqual(tell_when__100_years_old('rein', 30), 'Rein will be 100 at 2093.')

    def test_3(self):
        self.assertEqual(tell_when__100_years_old('rein', 40), 'Rein will be 100 at 2083.')

    def test_4(self):
        self.assertEqual(repeat_message("python", 3), "python\npython\npython")

    def test_5(self):
        self.assertEqual(repeat_message("python", 5), "python\npython\npython\npython\npython")
    
    def test_6(self):
        self.assertEqual(repeat_message("python", 7), "python\npython\npython\npython\npython\npython\npython")

if __name__ == '__main__':
    unittest.main()