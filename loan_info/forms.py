from django import forms

from .models import LoanDetail


class LoanDetailForm(forms.ModelForm):
    loan_name               = forms.CharField()
    loan_interest_rate       = forms.DecimalField(max_digits=5, decimal_places=4)
    loan_payment            = forms.DecimalField(max_digits=9, decimal_places=2)
    loan_current_balance    = forms.DecimalField(max_digits=9, decimal_places=2)
    previous_balance        = forms.DecimalField(max_digits=9, decimal_places=2)
    class Meta:
        model = LoanDetail
        fields = [
            'loan_name',
            'loan_interest_rate',
            'loan_payment',
            'loan_current_balance',
            'previous_balance',
            'interest_monthly',
        ]