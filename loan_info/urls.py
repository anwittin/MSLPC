from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.loan_create_view, name='loan-create'),
    path('loan_detail/<int:id>/', views.loan_detail_view, name='loan-detail'),
]