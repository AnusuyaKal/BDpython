import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertEqual(2 * 3, 5)  # This will fail

    def test_division(self):
        self.assertEqual(6 / 2, 3)

if __name__ == "__main__":
    unittest.main(Failfast=True)
