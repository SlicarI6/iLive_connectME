from django.contrib import admin
from .models import CustomUser  # importă modelul

admin.site.register(CustomUser)  # înregistrează modelul în admin
