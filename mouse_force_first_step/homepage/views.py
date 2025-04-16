from mouse_force_first_step.mycookieprivacy.models import UserCookies
from django.utils.timezone import now
from django.shortcuts import render
def index(request):
    user_ip = request.META.get('REMOTE_ADDR')
    already_set = UserCookies.objects.filter(user_ip=user_ip).exists()
    return render(request, 'index.html', {'show_cookie_banner': True})
# return render(request, 'index.html', {'show_cookie_banner': not already_set})

