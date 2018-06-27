# In Problem 1, we computed an exponential by iteratively executing successive multiplications.
# We can use the same idea, but in a recursive function.

# Write a function recurPower(base, exp) which computes
# by recursively calling itself to solve a smaller version of the same problem,
# and then multiplying the result by base to solve the initial problem.

# This function should take in two values - base can be a float or an integer;
# exp will be an integer ≥0.
#
# It should return one numerical value.
#
# Your code must be recursive
# - use of the ** operator or looping constructs is not allowed.
import unittest
from unittest import TestCase


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    if exp == 0:
        return 1.0

    else:
        return base*recurPower(base, exp-1)

class recurPowerTest(TestCase):

    def test_returns_2_to_power_2(self):
        base = 2
        exp = 2
        response = recurPower(base, exp)
        self.assertEqual(response, 4)

    def test_returns_2_to_power_3(self):
        base = 2
        exp = 3
        response = recurPower(base, exp)
        self.assertEqual(response, 8)

    def test_minus_3_power_0(self):
        base = -3.15
        exp = 0
        response = recurPower(base, exp)
        self.assertEqual(response, 1.0000)

    def test_minus_7_power_3(self):
        base = -7.03
        exp = 3
        response = recurPower(base, exp)
        self.assertEqual(response, -356.4008)

    def test_3_power_0(self):
        base = 3.89
        exp = 0
        response = recurPower(base, exp)
        self.assertEqual(response, 1.0000)

    def test_minus_9_power_10(self):
        base = -9.08
        exp = 10
        response = recurPower(base, exp)
        self.assertEqual(response, 3809416733.8292)


unittest.main

