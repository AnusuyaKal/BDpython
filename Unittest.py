import unittest

def sum(a,b):
    return a+b
# UnitTest Class derived and the functions inside the unitest class will be invoked
class SumTest(unittest.TestCase):
    def setUp(self):
        self.a=10
        self.b=20
        print("Self is called")
    def tearDown(self):
        self.a=0
        self.b=0
        print("Teardown is called")
    def test_sumfunc_1(self):
        print("Test 1 is Called")
        #Act
        result=sum(self.a,self.b)
        #Assert
        self.assertEqual(result,self.a+self.b)

    def test_sumfunc_2(self):#
        print("Test 2 is called")
        #Act
        result=sum(self.b,self.a)
        #Assert
        self.assertEqual(result,self.a+self.b)
    
# Invoke Unit Test Framework    
if __name__ == "__main__" :
    unittest.main()