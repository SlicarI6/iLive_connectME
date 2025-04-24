from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return request.user.is_staff
    
    
    
## Si eu pot sa il stilez acest admin sa imi arata doar acelea care sunt in migrations