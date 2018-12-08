from django.contrib import admin
from .models import PaymentGoals, PaymentInfo
# Register your models here.

admin.site.register([PaymentGoals, PaymentInfo])