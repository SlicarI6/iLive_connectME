from django.shortcuts import render
from django.http import JsonResponse
from .models import UserCookies
from django.utils.timezone import now

def accept_cookies(request):
    user_ip = request.META.get('REMOTE_ADDR')  
    accepted = request.GET.get('accepted', 'false') == 'true'  
    
    # Salvăm acceptarea în baza de date
    UserCookies.objects.create(user_ip=user_ip, accepted_cookies=accepted, accepted_at=now())

    # Creăm răspunsul JSON și setăm cookie-ul
    response = JsonResponse({'status': 'success', 'message': 'Cookies accepted' if accepted else 'Cookies rejected'})
    if accepted:
        response.set_cookie('cookies_accepted', 'true', max_age=31536000, httponly=True, secure=True, samesite='Lax')

        


    
    return response

def view_cookies(request):
    cookies_data = UserCookies.objects.all()
    return render(request, 'cookies/view_cookies.html', {'cookies_data': cookies_data})

# def view_cookies(request):
#     cookies_data = UserCookies.objects.all()
#     return render(request, 'cookies/view_cookies.html', {'cookies_data': cookies_data})