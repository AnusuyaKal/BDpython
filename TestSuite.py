import unittest

# Define test cases
class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

# Create a test suite
def create_test_suite():
    suite = unittest.TestSuite()#is a container that aggregates tests and provides a way to run them as a single unit. 
    suite.addTest(TestAddition('test_addition'))  # Add individual test case
    suite.addTest(TestSubtraction('test_subtraction'))  # Add individual test case
    return suite

if __name__ == '__main__':
    # Run the test suite
    test_suite = create_test_suite()
    unittest.TextTestRunner().run(test_suite)
