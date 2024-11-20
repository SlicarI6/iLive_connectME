# Crearea unui View pentru a salva acceptarea cookies:

from django.shortcuts import render
from django.http import JsonResponse
from .models import UserCookies
from django.utils.timezone import now

def accept_cookies(request):
    user_ip = request.META.get('REMOTE_ADDR')  # Obținem IP-ul utilizatorului
    accepted = request.GET.get('accepted', 'false') == 'true'  # Verificăm dacă utilizatorul a acceptat cookie-urile
    # Creăm un nou obiect UserCookies cu datele corespunzătoare
    UserCookies.objects.create(user_ip=user_ip, accepted_cookies=accepted, accepted_at=now())
    # Răspundem cu un mesaj JSON
    return JsonResponse({'status': 'success', 'message': 'Cookies accepted' if accepted else 'Cookies rejected'})

def view_cookies(request):
    cookies_data = UserCookies.objects.all()  # Preia toate înregistrările din modelul UserCookies
    return render(request, 'cookies/view_cookies.html', {'cookies_data': cookies_data})