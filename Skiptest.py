import unittest

class TestExample(unittest.TestCase):
    @unittest.skip("Skipping this test method for demonstration purposes")
    def test_skip(self):
        self.assertTrue(False)

    @unittest.skipIf(True, "Condition is True, skipping this test method")
    def test_skip_if(self):
        self.assertTrue(False)

    @unittest.skipUnless(False, "Condition is False, skipping this test method")
    def test_skip_unless(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
