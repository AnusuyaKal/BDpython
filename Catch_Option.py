import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        # This will raise an exception
        raise ValueError("Error in setup")

    def test_example(self):
        self.assertTrue(True)
        print('yes')

if __name__ == '__main__':
    unittest.main()
