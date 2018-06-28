# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#
# Lowest Payment: 180
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
#
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

from unittest import TestCase

def CreditCardBalanceClear(balance, annualInterestRate):
    """
    :param balance: float of starting balance for credit card
    :param annualInterestRate: float of annualised interest rate
    :return: lowest monthly payment to pay off in one year, must be multiple of 10 same for each month
    """
    # iterate over 12 months across a year

    # base case if min_payment is enough to clear balance return min_payment amount
    balance_with_interest = balance
    min_payment = 10
    while min_payment <= balance_with_interest:
        # re-set temp balanace marker each loop
        balance_with_interest = balance

        for months in range(1, 12+1):
            # calculate interest payment
            interest = balance_with_interest * (annualInterestRate/12)
            # add interest to balance
            balance_with_interest += interest

            # take payment away from balance
            balance_with_interest -= min_payment
        min_payment += 10
    print("found min value: " + str(min_payment))
    return min_payment

# define tests
class TestCreditCardBalanceClear(TestCase):

    def test_balance_3329_interest_0_2(self):
        balance = 3329
        annualInterestRate = 0.2

        response = CreditCardBalanceClear(balance, annualInterestRate)

        self.assertEqual(310, response)

    def test_balance_4773_interest_0_2(self):
        balance = 4773
        annualInterestRate = 0.2

        response = CreditCardBalanceClear(balance, annualInterestRate)

        self.assertEqual(440, response)

    def test_balance_3926_interest_0_2(self):
        balance = 3926
        annualInterestRate = 0.2

        response = CreditCardBalanceClear(balance, annualInterestRate)

        self.assertEqual(360, response)

    def test_balance_15780_interest_0_2(self):
        balance = 15780
        annualInterestRate = 0.2

        response = CreditCardBalanceClear(balance, annualInterestRate)

        self.assertEqual(1320, response)

