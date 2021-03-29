# Creating tests to check if the code can run without errors

# importting the file and class where the code is written
from simple_calc import SimpleCalc
import unittest

class CalcTest(unittest.TestCase):
    
    calc = SimpleCalc()

    #
    def test_add(self):
        # You must have 'test' in the name of these functions - if not, the python interpreter won't know 