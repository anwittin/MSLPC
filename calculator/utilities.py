import decimal
from datetime import datetime
# Calculator functions

# TODO: Create a calculator for daily compound interest 
# Forumla: (A = P(1 + r/n)^nt) 
# A = Total amount of money after n years 
# P = The Principal amount borrowed 
# r = the interest rate (per year) 
# n = the number of times interest is compounde per year 
# t = The time in years

r = float(input("Interest Rate: "))
p = float(input("Loan Amount(current ammount): "))
d1 = input("Date of last payment (as mm/dd/yy)")

n = float(365)
# Calculate the interest rate in decimal form
interest = decimal.Decimal(r)/100

days = datetime.now() - datetime.strptime(d1, "%m/%d/%y")
#TODO: Figure out how to calculate the days from the input (Previous payment - current date)
time_invested = days/365 
# Calculate for daily interest

#P(1 + (interest/365))**(365*time_invested)

class Loan:
    """Daily compounding interest for a loan."""
    def __init__(self, interest_rate, loan_value, last_payment_date, compound='daily'):
        """Initialize the loan
        Arguments:
        interest_rate as a float
        loan_value as"""
        self.interest_rate = interest_rate/100
        self.loan_value = loan_value
        self.last_payment_date = last_payment_date
        if compound == 'daily':
            self.compound_period = 365
    


