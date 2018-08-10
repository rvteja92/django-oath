from django.db import models

from django.conf import settings


SYMMETRIC_ALGORITHMS = {
    'AES': 'cryptography.hazmat.primitives.ciphers.algorithms.AES'
}

ALGORITHM_CHOICES = [(key, key) for key in SYMMETRIC_ALGORITHMS]

ENCRYPTION_MODES = {
    'CBC': 'cryptography.hazmat.primitives.ciphers.modes.CBC'
}

MODE_CHOICES = [(key, key) for key in ENCRYPTION_MODES]


# Create your models here.
class Tokens(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    seed = models.CharField(max_length=255)
    algorithm = models.CharField(max_length=10, choices=ALGORITHM_CHOICES)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
