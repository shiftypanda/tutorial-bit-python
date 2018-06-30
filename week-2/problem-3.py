# In short:
#
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# Write a program that uses these bounds and bisection search
# (for more info check out the Wikipedia page on bisection search)
# to find the smallest monthly payment to the cent (no more multiples of $10)
# such that we can pay off the debt within a year. Try it out with large inputs,
# and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!).
# Produce the same return value as you did in Problem 2.
#
# Note that if you do not use bisection search,
# your code will not run - your code only has 30 seconds to run on our servers.
from unittest import TestCase

balance = 100

annualInterestRate = 0.12

# bisection search
upper_limit = balance
lower_limit = 0
def find_min_payment(self):
    pass


print("Lowest Payment: " + str(minPayment))

# define test
class TestBisectionSearch(TestCase):

    def test_balanace_320000