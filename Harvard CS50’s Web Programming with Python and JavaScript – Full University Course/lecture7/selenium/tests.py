import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    """Returning the path of our filename."""
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# This shows up to our browswer
driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):
    """Testing the different attributes and methods in our webpage."""

    def test_title(self):
        """Checks the title of our html page."""
        # Creates an instance of our webpage
        driver.get(file_uri("counter.html")) 
        self.assertEqual(driver.title, "Counter")
    
    def test_increase(self):
        """Increase the counter in our webpage."""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element('id', 'increase')
        increase.click()
        self.assertEqual(driver.find_element('id', 'counter').text, "1")

    def test_decrease(self):
        """Decrease the counter in our webpage."""
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element('id', 'decrease')
        decrease.click()
        self.assertEqual(driver.find_element('id', 'counter').text, "-1")

    def test_multiple_increase(self):
        """Increase our counter multiple times."""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element('id', 'increase')
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element('id', 'counter').text, "3")

    def test_multiple_decrease(self):
        """Decrease our counter multiple times."""
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element('id', 'decrease')
        for i in range(3):
            decrease.click()
        self.assertEqual(driver.find_element('id', 'counter').text, "-3")

if __name__ == "__main__":
    unittest.main()