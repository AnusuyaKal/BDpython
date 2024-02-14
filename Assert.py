import unittest
class Test():
        pass

class Test1():
        pass
  
def is_even(number):
    return number % 2 == 0
   
class LearnUnitTest(unittest.TestCase):
    
    def test_sample(self):
        t1 = Test()
        t2 = Test()
        t3 = None
        #self.assertIs(t1,t2)
        #self.assertIsInstance(t1,Test)
        #self.assertIsNotNone(t3)
        #self.assertTrue(t1==t1)
        #self.assertTrue(is_even(4), "4 is an even number")

        #a=1
        #b=10
        #self.assertEqual(a,b,msg="A is not equal B")
        # self.assertNotEqual(a,b, msg="A is equal to B")
        #self.assertIs(a,b)
        #self.assertIsNot(a,b)
       
if __name__=="__main__":
    unittest.main()
    
    
