from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class PaymentInfo(models.Model):
    payment_date = models.DateField("Date of Payment")
    previous_payment = models.DateField("Date of Previous Payment")
    required_monthly = MoneyField("Required Payment", 
                                max_digits=10, 
                                decimal_places=2, 
                                default_currency='USD')
    extra_payment = MoneyField("Extra Payment", 
                                max_digits=10,
                                decimal_places=2,
                                default_currency='USD')
    
class PaymentGoals(models.Model):
    year_goal = models.DateField("Yearly Goal")
    loan_start = MoneyField("Period Loan Amount", 
                                max_digits=10,
                                decimal_places=2,
                                default_currency='USD')
    goal_amount = MoneyField("Goal Amount", 
                                max_digits=10,
                                decimal_places=2,
                                default_currency='USD')
    current_progress = MoneyField("Current Contribution",
                                max_digits=10,
                                decimal_places=2,
                                default_currency='USD')
    goal_percentage = models.DecimalField("Current Progress",
                                max_digits=5,
                                decimal_places=4)