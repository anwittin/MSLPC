from django.shortcuts import render, get_object_or_404

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

def loan_detail_view(request, id):
    obj = get_object_or_404(LoanDetail, id=id)
    context = {
        "object": obj
    }
    return render(request, "loan_detail.html", context)
