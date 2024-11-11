from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/index.html')  # Ruta către fișierul HTML din `templates/homepage`
