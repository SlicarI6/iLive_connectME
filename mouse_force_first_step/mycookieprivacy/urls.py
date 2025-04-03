from django.urls import path
from . import views
from django.urls import include, path
urlpatterns = [
    path('', views.privacy_policy, name='privacy_policy'),
    # other URL patterns
    # path('accept_cookies/', views.accept_cookies, name='accept_cookies'),
    
]