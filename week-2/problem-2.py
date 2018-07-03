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
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made).
# The monthly payment must be a multiple of $10 and is the same for all months.
# Notice that it is possible for the balance to become negative using this payment scheme,
# which is okay. A summary of the required math is found below:
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

    starting_balance = balance
    final_balance = balance

    def one_years_payment_simplified(balance, annualInterestRate, monthly_payment):
        """
        :param balance: starting balance
        :param annualInterestRate: dec annual interst
        :param monthly_payment: monthly payment amount
        :return: final balance after one years payment
        """
        temp_balance = balance
        for month in range(1, 12+1):

            # take payment away from balance
            temp_balance -= monthly_payment

            # calculate interest payment
            interest = temp_balance * (annualInterestRate / 12)

            # add interest to balance
            temp_balance = temp_balance + interest
        return temp_balance

    lowest_payment = 0  # initialise lowest_payment amount
    while lowest_payment <= final_balance:
        if final_balance <= 0:
            break
        elif final_balance > 0:
            lowest_payment += 10
            final_balance = one_years_payment_simplified(
                balance=starting_balance,
                annualInterestRate=annualInterestRate,
                monthly_payment=lowest_payment
            )

    print("Lowest Payment:", end=" ")
    print(str(lowest_payment))
    return lowest_payment

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

        self.assertEqual(1380, response)

    def test_balance_4872_interest_0_15(self):
        balance = 4872
        annualInterestRate = 0.15

        response = CreditCardBalanceClear(balance, annualInterestRate)

        self.assertEqual(440, response)

    def test_balance_448_interest_0_18(self):
        balance = 448
        annualInterestRate = 0.18

        response = CreditCardBalanceClear(balance, annualInterestRate)

        self.assertEqual(50, response)