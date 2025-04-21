from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser  # Sau poți folosi: from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from datetime import datetime
User = get_user_model()

def generate_unique_username(first_name, last_name, birth_date):
    base_username = f"{first_name.lower()}{last_name.lower()}"
    username = base_username

    birth_parts = []
    if birth_date:
        try:
            date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
            birth_parts = [str(date_obj.year)[-2:], str(date_obj.day), str(date_obj.month)]
        except ValueError:
            pass  # format greșit sau necompletat

    suffix_index = 0
    while CustomUser.objects.filter(username=username).exists():
        suffix = birth_parts[suffix_index % len(birth_parts)] if birth_parts else str(suffix_index + 1)
        username = f"{base_username}{suffix}"
        suffix_index += 1

    return username


def customer_account_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'customer'
            user.backend = 'mouse_force_first_step.accounts.auth_backends.EmailOrUsernameBackend'
            user.save()
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/customer_account_signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('username')  # poate fi email sau username
        password = request.POST.get('password')
        selected_role = request.session.get('selected_role')

        user = authenticate(request, username=identifier, password=password)

        if user:
            print("ROL SELECTAT:", request.session.get('selected_role'))
            print("ROL USER:", user.role)
            # ✅ Restricție: Simple user trebuie să folosească doar email
            if selected_role == 'simple' and '@' not in identifier:
                messages.error(request, 'Simple Users must log in using email.')
                return render(request, 'registration/login.html')

            login(request, user)

            # ✅ Redirecționare în funcție de rol
            if selected_role == 'customer' and user.role == 'customer':
                return redirect('customer_dashboard')
            elif selected_role == 'simple' and user.role == 'user':
                return redirect('homepage')
            else:
                messages.error(request, 'Role mismatch.')
        else:
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'registration/login.html')




def select_role_view(request):
    if request.method == 'POST':
        selected_role = request.POST.get('role')
        request.session['selected_role'] = selected_role
        return redirect('login')  # Te redirecționează către login
    return render(request, 'registration/select_role.html')
