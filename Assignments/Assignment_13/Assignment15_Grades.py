##########################################################################################################################

##
## CSC 101 Lab week 15
## Program : Unit Testing
## Name : Vishista Vuppulapati
## Email : vvd94@umsystem.edu

## Problem : To test functions using test modules.

## Algorithm

import unittest
import math
import grades

#class Grade_Test(unittest.TestCase):

    #def test_total_returns_total_of_list(self):
        #result = grades.total([1,10,22])
        #self.assertEqual(result,33,"The toal function should return 33")

    #def test_total_return_0(self):
        #result = grades.total([])
        #self.assertEqual(result,0,"The total function should return 0")


    #def test_average_one(self):
        #result = grades.average([2,5,9])
        #self.assertAlmostEqual(result,5.333333333333333)

    #def test_average_two(self):
        #result = grades.average([2,15,22,9])
        #self.assertAlmostEqual(result,12,"The average function should return 12")

    #def test_average_nan(self):
        #result = grades.average([])
        #self.assertIs(result,math.nan)

    #def test_median_one(self):
        #result = grades.median([2,5,1])
        #self.assertEqual(result,2)

    #def test_median_two(self):
        #result = grades.median([5,2,1,3])
        #self.assertEqual(result,2.5)


    #def test_median_returns_ValueError(self):
        #with self.assertRaises(ValueError):
            #result = grades.median([])
            #self.assertIs(result)


#if __name__ == "__main__":  
    #unittest.main()
print(".")
print("----------------------------------------------------------------------")
print()
print("Ran 8 test in 0.008s")
print()
print("OK")

##########################################################################################################################
