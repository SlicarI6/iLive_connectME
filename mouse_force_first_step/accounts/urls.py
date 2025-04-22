from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view
from django.contrib.auth.views import LogoutView
from .views import login_view, select_role_view
from .views import customer_account_signup
from .views import simple_user_signup_view
urlpatterns = [
    
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('select-role/', select_role_view, name='select_role'),
    path('customer-signup/', customer_account_signup, name='customer_account_signup'),
    path('simple-user-signup/', simple_user_signup_view, name='simple_user_signup'),
]
