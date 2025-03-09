from django.urls import path
from . import views

urlpatterns = [
    path('cookies/accept_cookies/', views.accept_cookies, name='accept_cookies'),
    path('view_cookies/', views.view_cookies, name='view_cookies'),
    path('cookies/check_cookies/', views.check_cookies, name='check_cookies'),
]
