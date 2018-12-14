from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.loan_create_view, name='loan-create'),
]