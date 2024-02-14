import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 2, 3)

    def test_division_by_zero(self):
        # Intentional error: Division by zero
        with self.assertRaises(ZeroDivisionError):
            result = 5 / 0

if __name__ == '__main__':
    unittest.main()
