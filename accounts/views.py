
#accounts/views.py: Aici creezi logica pentru a prelua datele din formular și a le salva în baza de date.
# For adding login, logout, or registration logic

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contul a fost creat cu succes!")
            return redirect('login')
    else:
        form = SignUpForm()  # Use SignUpForm here
    return render(request, 'registration/signup.html', {'form': form})
