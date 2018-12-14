from django.db import models
# Create your models here.

class LoanDetail(models.Model):
    loan_name               = models.CharField(max_length=50)
    loan_intrest_rate       = models.DecimalField(max_digits=5, decimal_places=4)
    loan_payment            = models.DecimalField(max_digits=9, decimal_places=2)
    loan_current_balance    = models.DecimalField(max_digits=9, decimal_places=2)