
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
                                 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mouse_force_first_step.homepage.urls')),
    path('accounts/', include('mouse_force_first_step.accounts.urls')),  # Asigură-te că are prefix
    path('myapp/', include('mouse_force_first_step.myapp.urls')),
    path('privacy_policy/', include('mouse_force_first_step.mycookieprivacy.urls')),
    path('customer/', include('mouse_force_first_step.customerpanel.urls')),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)