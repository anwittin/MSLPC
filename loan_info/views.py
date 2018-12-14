from django.shortcuts import render

# Create your views here.
from .forms import LoanDetailForm
from .models import LoanDetail


def loan_create_view(request):
    form = LoanDetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LoanDetailForm()
    context = {
        'form': form
    }

    return render(request, "loan_create.html", context)