import unittest
import math_operations

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_operations.add(1, 2), 3)
        self.assertEqual(math_operations.add(-1, 1), 0)
        self.assertEqual(math_operations.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(math_operations.subtract(5, 2), 3)
        self.assertEqual(math_operations.subtract(5, 5), 0)
        self.assertEqual(math_operations.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(math_operations.multiply(2, 3), 6)
        self.assertEqual(math_operations.multiply(5, 0), 0)
        self.assertEqual(math_operations.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(math_operations.divide(6, 3), 2)
        self.assertEqual(math_operations.divide(5, 2), 2.5)
        self.assertRaises(ValueError, math_operations.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()