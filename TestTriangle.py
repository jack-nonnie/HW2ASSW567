# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from HW2ASSW567.Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNegativeA(self):
        self.assertEqual(classifyTriangle(-4,3,2), "InvalidInput", "Triangles cannot have negative side lengths -4,3,2 is invalid")

    def testNegativeB(self):
        self.assertEqual(classifyTriangle(4,-3,2), "InvalidInput", "Triangles cannot have negative side lengths 4,-3,2 is invalid")

    def testNegativeC(self):
        self.assertEqual(classifyTriangle(4,3,-2), "InvalidInput", "Triangles cannot have negative side lengths 4,3,-2 is invalid")

    def testTooLargeA(self):
        self.assertEqual(classifyTriangle(130,130,230), "InvalidInput", "130,130,230: Inputs should not be larger than 200")

    def testTooLargeB(self):
        self.assertEqual(classifyTriangle(130,630,30), "InvalidInput", "130,630,30: Inputs should not be larger than 200")

    def testTooLargeC(self):
        self.assertEqual(classifyTriangle(301,130,30), "InvalidInput", "301,130,30: Inputs should not be larger than 200")

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(2,5,8), "NotATriangle", "One side of a triangle cannot be larger than the other two sides")

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(4,10,6), "NotATriangle", "One side of a triangle cannot be equal to the sum of the other two sides")

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,4), "Right", "3,5,4 is a Right triangle")

    def testScaleneA(self):
        self.assertEqual(classifyTriangle(2,4,5), "Scalene", "2,4,5 is a Scalene triangle")

    def testScaleneB(self):
        self.assertEqual(classifyTriangle(6,9,5), "Scalene", "6,9,5 is a Scalene triangle")

    def testIsoA(self):
        self.assertEqual(classifyTriangle(4,4,6), "Isosceles", "4,4,6 is an Isosceles triangle")

    def testIsoB(self):
        self.assertEqual(classifyTriangle(8,4,8), "Isosceles", "8,4,8 is an Isosceles triangle")

    def testIsoC(self):
        self.assertEqual(classifyTriangle(4,3,3), "Isosceles", "4,3,3 is an Isosceles triangle")




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

