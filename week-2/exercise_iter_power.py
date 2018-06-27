# Write an iterative function iterPower(base, exp) that
# calculates the exponential

# by simply using successive multiplication. For example,
# iterPower(base, exp) should compute
# by multiplying base times itself exp times.
# Write such a function below.

# This function should take in two values - base can be a float or an
# integer; exp will be an integer
# ≥
# 0. It should return one numerical value. Your code must be
# iterative - use of the ** operator is not allowed.
from unittest import TestCase
import unittest

def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

# NOTE: read the questinos properly it was dont use ** exponentiatl rather than don't use * multiply, arGH!!!!


class IterPowerTest(TestCase):

    def test_returns_2_to_power_2(self):
        base = 2
        exp = 2
        response = iterPower(base, exp)
        self.assertEqual(response, 4)

    def test_returns_2_to_power_3(self):
        base = 2
        exp = 3
        response = iterPower(base, exp)
        self.assertEqual(response, 8)

    def test_minus_3_power_0(self):
        base = -3.15
        exp = 0
        response = iterPower(base, exp)
        self.assertEqual(response, 1.0000)

    def test_minus_7_power_3(self):
        base = -7.03
        exp = 3
        response = iterPower(base, exp)
        self.assertEqual(response, -356.4008)

    def test_3_power_0(self):
        base = 3.89
        exp = 0
        response = iterPower(base, exp)
        self.assertEqual(response, 1.0000)

    def test_minus_9_power_10(self):
        base = -9.08
        exp = 10
        response = iterPower(base, exp)
        self.assertEqual(response, 3809416733.8292)

unittest.main()