# passwords/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet


class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def encrypt_password(self, raw_password):
        key = settings.FERNET_KEY.encode()  # Retrieve the key from settings
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(raw_password.encode())
        self.password = encrypted_password.decode()

    def decrypt_password(self):
        key = settings.FERNET_KEY.encode()  # Retrieve the key from settings
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(self.password.encode())
        return decrypted_password.decode()
