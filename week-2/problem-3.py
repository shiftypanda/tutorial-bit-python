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

def find_min_payment(balance, annualInterestRate):
    """
    :param balance: starting balance
    :param annualInterestRate: annual interest rate in decimal
    :return: decimal, minimum monthly payment to clear balance in 12 months
    """


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
            temp_balance = temp_balance + round(interest, 2)
        return round(temp_balance, 2)


    final_balance = balance

    min_payment = 259

    upper_limit = final_balance
    lower_limit = final_balance / 12.0

    epsilon = 0.01

    while final_balance != epsilon: # if final balanace = 0 then returns min payment


        if final_balance > epsilon: # if final balance is greater than 0, resets lower limit
            lower_limit = min_payment

        elif final_balance < epsilon :
            upper_limit = min_payment

        min_payment = (lower_limit + upper_limit) / 2.0

        final_balance = one_years_payment_simplified(
            balance,
            annualInterestRate,
            monthly_payment=min_payment
        )


    print("Lowest Payment: " + str(round(min_payment, 2)))
    # return round(min_payment, 2)

find_min_payment(balance, annualInterestRate)


# define test
class TestBisectionSearch(TestCase):

    def test_balanace_320000_rate_0_2(self):
        balance = 320000
        annualInterestRate = 0.2

        response = find_min_payment(balance, annualInterestRate)

        self.assertEqual(29157.09, response)

    def test_balanace_999999_rate_0_18(self):
        balance = 999999
        annualInterestRate = 0.18

        response = find_min_payment(balance, annualInterestRate)

        self.assertEqual(90325.03, response)