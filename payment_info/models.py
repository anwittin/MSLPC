from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from djmoney.models.fields import MoneyField

# Create your models here.

class PaymentInfo(models.Model):
    payment_info = models.TextField("Name of Loan", max_length=50, null=True)
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

    def __str__(self):
        return self.payment_info
    
class PaymentGoal(models.Model):
    payment_goal = models.TextField("Payment Goal Name", max_length=50, null=True)
    year_goal = models.PositiveIntegerField(
            validators=[
                MinValueValidator(2018), 
                MaxValueValidator(2100)],
            help_text="Use the following format: 20YY")
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
    
    def __str__(self):
        return self.payment_goal