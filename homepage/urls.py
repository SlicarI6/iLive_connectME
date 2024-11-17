from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Route to the homepage
    path('cookie/', views.cookie, name='cookie'),  # Route to the cookie page
]
