# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance.
# Be sure to print out no more than two decimal digits of accuracy - so print
#
# Remaining balance: 813.41
# instead of
#
# Remaining balance: 813.4141998135
# So your program only prints out one thing:
# the remaining balance at the end of the year in the format:
#
# Remaining balance: 4784.0
# A summary of the required math is found below:
#
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#
# We provide sample test cases below.
# We suggest you develop your code on your own machine,
# and make sure your code passes the sample test cases,
# before you paste it into the box below.
#
# Test Cases to Test Your Code With.
# Be sure to test these on your own machine -
# and that you get the same output! -
#  before running your code on this webpage!

# always start with importing unittest TestCase because this is test driven development!
from unittest import TestCase

def CreditCardBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    :param balance: float of starting balance for credit card
    :param annualInterestRate: float of annualised interest rate
    :param monthlyPaymentRate: float of monthly payment
    :return: remaining balance after 12 months of payments accounting for interest
    """
    # iterate over 12 months across a year

    for months in range(1, 12+1):
        # calculate interest payment
        interest = balance * (annualInterestRate/12)
        # add interest to balance
        balance += interest

        # calculate minimum payment with interest already included
        payment = balance * monthlyPaymentRate
        # take payment away from balance
        balance -= payment

    problem_one = round(balance, 2)
    print("Remaining balance: " + str(problem_one))
    return round(balance, 2)


# define tests
class TestCreditCardBalance(TestCase):

    def test_balance_42_interest_02_monthly_payments_0_04(self):
        balance = 42
        annualInterestRate = 0.2
        monthlyPaymentRate = 0.04

        response = CreditCardBalance(balance, annualInterestRate, monthlyPaymentRate)

        self.assertEqual(31.38, response)

    def test_balance_484_interest_02_monthly_payments_0_04(self):
        balance = 484
        annualInterestRate = 0.2
        monthlyPaymentRate = 0.04

        response = CreditCardBalance(balance, annualInterestRate, monthlyPaymentRate)

        self.assertEqual(361.61, response)