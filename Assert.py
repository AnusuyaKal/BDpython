# import unittest

# def add(a, b):
#     return a + b

# class TestAssertFunctions(unittest.TestCase):

#     def test_assert_equal(self):
#         self.assertEqual(add(2, 3), 5)
    
#     def test_assert_not_equal(self):
#         self.assertNotEqual(add(2, 3), 6)

#     def test_assert_true(self):
#         self.assertTrue(add(2, 3) == 5)

#     def test_assert_false(self):
#         self.assertFalse(add(2, 3) == 6)

#     def test_assert_in(self):
#         self.assertIn('a', 'banana')

#     def test_assert_not_in(self):
#         self.assertNotIn('z', 'banana')

#     def test_assert_is_none(self):
#         self.assertIsNone(None)

#     def test_assert_is_not_none(self):
#         self.assertIsNotNone(add(2, 3))

# if __name__ == '__main__':
#     unittest.main()

 

import unittest
class Test():
        pass

class Test1():
        pass
  
  
class LearnUnitTest(unittest.TestCase):
    
    def test_sample(self):
        t1 = Test()
        t2 = Test()
        t1=t2
        

        #self.assertIs(t1,t2)
        self.assertIsInstance(t1,Test)
      
        
        
              
if __name__=="__main__":
    unittest.main()
        
    
# import unittest

# class TestSkip(unittest.TestCase):

#     @unittest.skip("Skipping this test method for demonstration purposes")
#     def test_skip(self):
#         # This test method will be skipped
#         self.assertTrue(False)

#     def test_normal(self):
#         # This test method will run normally
#         self.assertTrue(True)

# if __name__ == '__main__':
#     unittest.main()