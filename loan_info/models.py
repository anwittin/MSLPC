from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class LoanDetail(models.Model):
    loan_name               = models.CharField(max_length=50)
    loan_intrest_rate       = models.DecimalField(max_digits=5, decimal_places=4)
    loan_payment            = MoneyField(max_digits=9, decimal_places=2)
    loan_current_balance    = MoneyField(max_digits=9, decimal_places=2)


    def __str__(self):
        return self.loan_name