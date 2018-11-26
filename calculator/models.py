from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

STATUS_CHOICES = (
    # User choices for status of loan.
    # TODO: Use status to factor interest
    ('ACTIVE', 'Active'),
    ('DEFERMENT', 'Deferment'),
    ('FORBEARANCE', 'Forebarance'),
    ('DEFAULT', 'Default'),
    ('EXCLUDED', 'Excluded'),
    ('PAID OFF', 'Paid Off'),
)
ACCOUNT_CHOICES = (
    ('STAFFORD_SUB', 'Federal Stafford Loan (Subsidized)'),
    ('STAFFORD_UNSUB', 'Federal Stafford Loan (Unsubsidized)'),
    ('PERKINS', 'Federal Perkins Loan'),
    ('PRIVATE', 'Private Lender'),
    ('PLUS', 'Parent Loans for Undergradate Students'),
    ('FAMILY', 'Family'),
    ('PERSONAL', 'Personal'),
    ('GRADPLUS', 'Grad Plus'),
    ('OTHER_LOAN', 'Other Student Loan'),
)

class Account(models.Model):
    # Name of each loan the user has
    loan = models.CharField("Loan Name", max_length=75)
    # Type of student loan the user has. 
    # TODO: Build calculator for loan types
    account_type = models.CharField("Account Type", 
                                max_length= 50, 
                                choices=ACCOUNT_CHOICES)
    # Interest rate of each loan as a number, will need to convert
    # to a percentage (/100)
    rate = models.DecimalField("Interest Rate", 
                                max_digits=8, 
                                decimal_places=5)
    # What the orginal loan dispercment was.
    start_balance = MoneyField("Beginning Balance", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')
    # Current loan balance, can be higher than orginal.
    balance = MoneyField("Current Loan Balance",
                                max_digits=10, 
                                decimal_places=2,
                                default_currency='USD')
    # Balance at the end of the previous month
    # TODO: calculate monthly interest - payment to get end balance.
    previous_balance = MoneyField("Previous Months Balance", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')
    # Minimum required payment for the loan by the bank
    payment = MoneyField("Payment Amount", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')
    # Monthly interest accrual. 
    # TODO: figure out how to make uneditable but still visible. 
    # TODO: Add calculation to field.
    monthly = MoneyField("Monthly Interest Amount", 
                                max_digits=10,
                                decimal_places=2,
                                default_currency='USD')
    # Current loan status.
    # TODO: Calculators will need to take status into calculations
    # (ie deferment intrest accrues but 0 payment) 
    status = models.CharField("Loan Status", 
                                max_length=10, 
                                choices=STATUS_CHOICES)
    # Current date payment is due
    due_date = models.DateField("Payment Due Date")
    # How much the user paid on the loan
    paid = MoneyField("Current Amount Paid", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')

    def __str__(self):
        return self.loan

