"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('homepage.urls')),  # This will route the homepage
#     path('accounts/', include('Mouseforce.accounts.urls')),
#     path('myapp/', include('myapp.urls')),
#     path('privacy_policy/', include('mycookieprivacy.urls')),
#     path('', include('cookies.urls')),
# ]                                    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mouseforce.homepage.urls')),
    path('accounts/', include('Mouseforce.accounts.urls')),  # Asigură-te că are prefix
    path('myapp/', include('Mouseforce.myapp.urls')),
    path('privacy_policy/', include('Mouseforce.mycookieprivacy.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)