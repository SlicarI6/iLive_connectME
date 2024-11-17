from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/index.html')  # Ensure this file exists in the `templates/homepage` directory

def cookie(request):
    return render(request, 'homepage/cookie.html')  # Ensure this file exists in the `templates/homepage` directory
