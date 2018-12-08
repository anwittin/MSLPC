from django.contrib import admin
from .models import PaymentGoal, PaymentInfo
# Register your models here.

admin.site.register([PaymentGoal, PaymentInfo])