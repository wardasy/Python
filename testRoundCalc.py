#Name: Wardah Shekh Yousef ID: 209011501
#Name: Naseem Ali  ID: 312343668

import roundCalc
import unittest


class TestCalc(unittest.TestCase):
    def testRoundUpMul(self):
        ''' check if the round up fail when negative or zero '''
        self.assertEqual(roundCalc.roundUpMul(0 , 4) , 10)#check what happened when you type one zero
        self.assertEqual(roundCalc.roundUpMul(-3 , 4) , -10) #check what happened when you type one negative number
    
    def testRoundDownMul(self):
        ''' check if the round down fail when negative or zero '''
        self.assertEqual(roundCalc.roundDownMul(-3 , 4) , -20) #check the round down with negative
        self.assertEqual(roundCalc.roundDownMul(0 , 4) , 0) #check the round down when you reach zero
        
    def testRoundMax(self):
        ''' check if the round max fail when different round up or zero '''
        self.assertEqual(roundCalc.roundMax(13 , 24) , 30) #check two numbers with two different round Up
        self.assertEqual(roundCalc.roundMax(0 , 4) , 10) #check with zero
        
    def testRoundUpOrDown(self):
        ''' check if the get the round up fail when unexpected number or zero '''
        self.assertEqual(roundCalc.GetRoundNum(0 , 0) , 0) #check zero round down
        self.assertEqual(roundCalc.GetRoundNum(0 , 1) , 10) #check zero round up
        self.assertEqual(roundCalc.GetRoundNum(0 , 2) ,-1) #check wrong Input
        
        
if __name__ == "__main__":
    unittest.main()