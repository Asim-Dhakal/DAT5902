import unittest
from Week2 import NumberIsEven
class TestFunction(unittest.TestCase):

    #tests with Odd number
    def test_Odd_number(self):
        result = NumberIsEven(5)
        self.assertEqual(result, False)

    # tests with Even number 
    def test_Even_number(self):
        result = NumberIsEven(4)
        self.assertEqual(result, True)

    # tests with Odd number 
    def test_None_number(self):
        result = NumberIsEven('String')
        self.assertEqual(result, False)
        
if __name__ == '__main__':
    unittest.main()