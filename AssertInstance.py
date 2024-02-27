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
        t3 = None

        #self.assertIs(t1,t3)
        #self.assertIsInstance(t1,Test)
        #self.assertIsNotNone(t3)
        
        
              
if __name__=="__main__":
    unittest.main()
    