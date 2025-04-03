from django.urls import path
from . import views
from mouse_force_first_step.mycookieprivacy import views as cookie_views


urlpatterns = [
    
    path('', views.index, name='index'),
    # path('accept_cookies/', views.accept_cookies, name='accept_cookies'),
    path('accept_cookies/', cookie_views.accept_cookies, name='accept_cookies'),

    
]
