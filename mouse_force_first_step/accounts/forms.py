from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        # Generate base username
        base_username = f"{self.cleaned_data['first_name'].lower()}{self.cleaned_data['last_name'].lower()}"

        # Add digits from birth_date if needed
        birth_date = self.cleaned_data.get('birth_date')
        suffix = str(birth_date.year)[-2:] if birth_date else ''
        username = base_username
        if CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{suffix}"
            if CustomUser.objects.filter(username=username).exists():
                username = f"{base_username}{suffix}{birth_date.day}"

        user.username = username
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user