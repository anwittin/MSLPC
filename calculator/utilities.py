import datetime, decimal
# Calculator functions

# TODO: Create a calculator for daily compound interest 
# Forumla: (A = P(1 + r/n)^nt) 
# A = Total amount of money after n years 
# P = The Principal amount borrowed 
# r = the interest rate (per year) 
# n = the number of times interest is compounde per year 
# t = The time in years

r = float(input("Interest Rate: "))
p = int(input("Loan Amount(current ammount): "))
t1 = int(input("Date of last payment (as mm/dd/yyyy)"))
t2 = todays date
n = float(365.25)
# Calculate the interest rate in decimal form
interest = Decimal(r)/100
days = t2 - t1
#TODO: Figure out how to calculate the days from the input (Previous payment - current date)
time_invested = days/365 
# Calculate for daily interest
P(1 + (interest/365))**(365*time_invested)

