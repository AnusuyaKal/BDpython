import unittest

def is_even(number):
    return number % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        # Test even number
        #self.assertTrue(is_even(5), "5 is not an even number")

        # Test odd number
        self.assertFalse(is_even(4), "4 is an even number")

if __name__ == "__main__":
    unittest.main()
