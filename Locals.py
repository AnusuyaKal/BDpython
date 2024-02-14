import unittest

class TestExample(unittest.TestCase):
    def test_failure(self):
        x = 10
        y = 5
        self.assertEqual(x, y, "This assertion will fail")

# if __name__ == '__main__':
#     unittest.main()
