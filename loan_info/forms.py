from django import forms


class LoanDetail(forms.Form):
    loan_name               = forms.CharField()
    loan_intrest_rate       = forms.DecimalField(max_digits=5, decimal_places=4)
    loan_payment            = forms.DecimalField(max_digits=9, decimal_places=2)
    loan_current_balance    = forms.DecimalField(max_digits=9, decimal_places=2)
    