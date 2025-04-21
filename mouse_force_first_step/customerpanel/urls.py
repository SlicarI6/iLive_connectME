from django.urls import path
from .views import customer_dashboard

urlpatterns = [
    path('dashboard/', customer_dashboard, name='customer_dashboard'),
    
]