from django.db import models

#Creează un model de date pentru a salva cine a acceptat cookies: În fișierul cookies/models.py

class UserCookies(models.Model):
    user_ip = models.GenericIPAddressField()  # Salvează IP-ul utilizatorului
    accepted_cookies = models.BooleanField(default=False)  # True dacă cookies sunt acceptate, altfel False
    accepted_at = models.DateTimeField()  # Data și ora în care utilizatorul a acceptat sau respins cookies

    def __str__(self):
        return f"Cookies accepted by {self.user_ip} on {self.accepted_at}"
