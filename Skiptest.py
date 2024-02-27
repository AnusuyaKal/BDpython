import unittest

class TestSkip(unittest.TestCase):

    @unittest.skip("Skipping this test method for demonstration purposes")
    def test_skip(self):
        # This test method will be skipped
        self.assertTrue(False)

    def test_normal(self):
        # This test method will run normally
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
