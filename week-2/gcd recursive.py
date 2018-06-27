# greatest common divisor of two positive intgers
import unittest
from unittest import TestCase


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    # base case is when b = 0
    if b == 0:
        return a
    # recursive case
    return gcdRecur(b, a % b)



class TestGcdIter(TestCase):

    def test_2_and_12(self):
        a = 2
        b = 12
        response = gcdRecur(a, b)
        self.assertEqual(response, 2)

    def test_6_and_12(self):
        a = 6
        b = 12
        response = gcdRecur(a, b)
        self.assertEqual(response, 6)

    def test_9_and_12(self):
        a = 9
        b = 12
        response = gcdRecur(a, b)
        self.assertEqual(response, 3)

    def test_17_and_12(self):
        a = 17
        b = 12
        response = gcdRecur(a, b)
        self.assertEqual(response, 1)