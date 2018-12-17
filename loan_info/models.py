from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class LoanDetail(models.Model):
    loan_name               = models.CharField(max_length=50)
    loan_interest_rate       = models.DecimalField(max_digits=5, decimal_places=2)
    loan_payment            = MoneyField("Payment Amount", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')
    loan_current_balance    = MoneyField("Current Loan Balance",
                                max_digits=10, 
                                decimal_places=2,
                                default_currency='USD')
    previous_balance    = MoneyField("Previous Balance",
                                max_digits=10, 
                                decimal_places=2,
                                default_currency='USD')
    interest_monthly            = MoneyField("Monthly Interest", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')


    def __str__(self):
        return self.loan_name