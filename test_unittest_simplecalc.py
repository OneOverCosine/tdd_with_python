# Creating tests to check if the code can run without errors

# importting the file and class where the code is written
from simple_calc import SimpleCalc
import unittest

class CalcTest(unittest.TestCase):
    
    calc = SimpleCalc()

    #
    def test_add(self):
        # You must have 'test' in the name of these functions - if not, the python interpreter won't know what to test
        # checks that 2 + 4 = 6 using the add method that was implemented
        self.assertEqual(self.calc.add(2, 4), 6) # returns True if it passes

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(21, 3), 7)