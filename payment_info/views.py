from django.shortcuts import render
from django.http import HttpResponse

from .models import PaymentGoal, PaymentInfo

# Create your views here.

def index(request):
    payment_goal = PaymentGoal.objects.