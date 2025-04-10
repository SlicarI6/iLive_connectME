
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

from mouse_force_first_step.mycookieprivacy.models import UserCookies

from mouse_force_first_step.mycookieprivacy.models import UserCookies
from .models import UserCookies


def privacy_policy(request):
    if request.method == 'GET':
        return render(request, 'privacy_policy.html')  # sau numele corect al template-ului

    if request.method == 'POST':
        try:
            print("📥 Request Body (RAW):", request.body)  # ← Afișează datele primite în POST
            
            data = json.loads(request.body)
            advertising = data.get('advertising', False)
            analytics = data.get('analytics', False)
            personalisation = data.get('personalisation', False)
            user_ip = request.META.get('REMOTE_ADDR', 'unknown')
            print(f"IP: {user_ip}, Advertising: {advertising}, Analytics: {analytics}, personalisation{personalisation}")

            print("✅ Date salvate:", advertising, analytics, personalisation, user_ip)

            UserCookies.objects.create(
                user_ip=user_ip,
                accepted_cookies=True,
                functional_advertising=advertising,
                functional_analytics=analytics,
                functional_personalisation=personalisation,
                accepted_at=now()
            )

            return JsonResponse({'status': 'success', 'message': 'Preferences saved'})
        except Exception as e:
            print("⚠️ Eroare:", str(e))  # ← Afișează erorile în terminal
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def accept_cookies(request):
    if request.method == 'POST':
        try:
            # Citește datele trimise în body-ul cererii
            data = json.loads(request.body)
            accepted_cookies = data.get('accepted', False)

            # Obține IP-ul utilizatorului
            user_ip = request.META.get('REMOTE_ADDR')

            # Salvează consimțământul în baza de date
            UserCookies.objects.create(
                user_ip=user_ip,
                accepted_cookies=accepted_cookies,
                functional_advertising=False,  # Poți modifica în funcție de alegerea utilizatorului
                functional_analytics=False,
                functional_personalisation=True
            )

            # Răspunsul pozitiv
            return JsonResponse({'status': 'success', 'message': 'Cookies accepted'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)