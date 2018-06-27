# The greatest common divisor of two positive integers is the
# largest integer that divides each of them without remainder.
#
# For example,
#
# gcd(2, 12) = 2
#
# gcd(6, 12) = 6
#
# gcd(9, 12) = 3
#
# gcd(17, 12) = 1
#
# Write an iterative function, gcdIter(a, b),
# that implements this idea.
#
# One easy way to do this is to begin with a test value equal to the smaller of the two input arguments,
# and iteratively reduce this test value by 1 until you either reach a case
# where the test divides both a and b without remainder,
# or you reach 1.

import unittest
from unittest import TestCase

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testValue = min(a, b)

    # loop until testValue divides both a and b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue




class TestGcdIter(TestCase):

    def test_2_and_12(self):
        a = 2
        b = 12
        response = gcdIter(a, b)
        self.assertEqual(response, 2)

    def test_6_and_12(self):
        a = 6
        b = 12
        response = gcdIter(a, b)
        self.assertEqual(response, 6)

    def test_9_and_12(self):
        a = 9
        b = 12
        response = gcdIter(a, b)
        self.assertEqual(response, 3)

    def test_17_and_12(self):
        a = 17
        b = 12
        response = gcdIter(a, b)
        self.assertEqual(response, 1)