
from django.shortcuts import render
from django.http import JsonResponse

def privacy_policy(request):
    if request.method == 'POST':
        # Verificăm dacă utilizatorul a apăsat "Reject All" sau "Confirm My Choices"
        if 'reject_all' in request.POST:
            # Logică pentru a respinge toate cookie-urile
            response_data = {'status': 'success', 'message': 'Cookies rejected'}
            return JsonResponse(response_data)
        elif 'confirm_choices' in request.POST:
            # Logică pentru a confirma preferințele utilizatorului
            response_data = {'status': 'success', 'message': 'Cookies accepted'}
            return JsonResponse(response_data)

    return render(request, 'privacy_policy.html')
