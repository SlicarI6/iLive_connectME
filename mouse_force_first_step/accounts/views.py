from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser  # Sau poți folosi: from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from datetime import datetime
from django.core.mail import send_mail
from django.http import JsonResponse
import json
import random
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


def simple_user_signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/simple_user_signup.html', {
                'error': 'This email is already in use.'
            })

        user = User.objects.create_user(
            username=email.split('@')[0],  # simplu, dar unic
            email=email,
            password=password,
            role='simple'  # asigură-te că modelul tău are câmpul `role`
        )
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return render(request, 'init_session.html')

    return render(request, 'registration/simple_user_signup.html')


def customer_account_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            base_username = f"{user.first_name.lower()}{user.last_name.lower()}"
            username = base_username
            attempts = 0

            while CustomUser.objects.filter(username=username).exists():
                suffix = random.randint(1, 999)
                username = f"{base_username}{suffix}"
                attempts += 1
                if attempts > 5:
                    username = f"{base_username}{random.randint(1000, 9999)}"
                    break

            user.username = username
            user.role = 'customer'
            user.backend = 'mouse_force_first_step.accounts.auth_backends.EmailOrUsernameBackend'
            user.save()
            login(request, user)
            return render(request, 'init_session.html')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/customer_account_signup.html', {'form': form})


def login_simple_user_view(request):
    request.session['selected_role'] = 'simple'

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user and user.role == 'simple':
            login(request, user)
            return redirect('homepage')  # 🔁 redirecționează spre homepage
        else:
            messages.error(request, "Invalid credentials or role mismatch.")

    return render(request, 'registration/login_simple_user.html', {'role': 'simple'})

def login_account_customer_view(request):
    request.session['selected_role'] = 'customer'

    if request.method == 'POST':
        identifier = request.POST.get('username')  # poate fi username sau email
        password = request.POST.get('password')

        user = authenticate(request, username=identifier, password=password)
        print("AUTH RESULT:", user)
        if user and user.role == 'customer':
            print("USER ROLE:", user.role)
            login(request, user)
            return redirect('customer_dashboard')  # 🔁 redirecționează spre dashboard-ul clientului
        else:
            messages.error(request, "Invalid credentials or role mismatch.")
    
    return render(request, 'registration/login_account_customer.html', {'role': 'customer'})




def select_role_view(request):
    if request.method == 'POST':
        selected_role = request.POST.get('role')
        request.session['selected_role'] = selected_role

        if selected_role == 'simple':
            return redirect('login_simple_user')
        else:
            return redirect('login_account_customer')

    return render(request, 'init_session.html')



def simple_user_password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email, role='simple')
            # Creează o parolă temporară (ex: 6 caractere simple)
            from django.utils.crypto import get_random_string
            new_password = get_random_string(6)
            user.set_password(new_password)
            user.save()

            # Trimite email
            send_mail(
                'Password Reset',
                f'Your new password is: {new_password}',
                'no-reply@example.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Check your email for the new password.')
        except User.DoesNotExist:
            messages.error(request, 'Email not found or invalid user.')
    return render(request, 'registration/password_reset_simple_user.html')


def check_email_exists_simple_user(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        email = data.get('email')
        exists = User.objects.filter(email=email, role='simple').exists()
        print("EMAIL PRIMIT:", email, "| EXISTS:", exists)
        return JsonResponse({'exists': exists})

def check_email_exists_customer_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        exists = User.objects.filter(email=email, role='customer').exists()
        print("CHECK CUSTOMER EMAIL:", email, "| EXISTS:", exists)
        return JsonResponse({'exists': exists})
    
    
def check_username_exists_customer_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        exists = User.objects.filter(username=username, role='customer').exists()
        return JsonResponse({'exists': exists})
    
    
def recover_username_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        try:
            user = User.objects.get(email=email, role='customer')
            return JsonResponse({'success': True, 'username': user.username})
        except User.DoesNotExist:
            return JsonResponse({'success': False})