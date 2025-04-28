from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from .views import  select_role_view
from .views import customer_account_signup
from .views import simple_user_signup_view
from .views import simple_user_password_reset_request

urlpatterns = [
    path('login/simple-user/', views.login_simple_user_view, name='login_simple_user'),
    path('login/customer-account/', views.login_account_customer_view, name='login_account_customer'),
    
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('select-role/', select_role_view, name='select_role'),
    path('customer-signup/', customer_account_signup, name='customer_account_signup'),
    path('simple-user-signup/', simple_user_signup_view, name='simple_user_signup'),
]
