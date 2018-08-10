from django.db import models
from django.conf import settings

from .defaults import app_settings


SYMMETRIC_ALGORITHMS = {
    'AES': 'cryptography.hazmat.primitives.ciphers.algorithms.AES'
}

ALGORITHM_CHOICES = [(key, key) for key in SYMMETRIC_ALGORITHMS]

ENCRYPTION_MODES = {
    'CBC': 'cryptography.hazmat.primitives.ciphers.modes.CBC'
}

MODE_CHOICES = [(key, key) for key in ENCRYPTION_MODES]

SECOND_STEP_METHODS = (
    ('TOTP', 'TOTP'),
    # HOTP to be added later
)


# Create your models here.
class Token(models.Model):
    # Using `ForeignKey` to support multiple devices, instead of `OneToOne`
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='oathtoken')
    seed = models.CharField(max_length=255)
    algorithm = models.CharField(max_length=10, choices=ALGORITHM_CHOICES)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    method = models.CharField(max_length=10, choices=SECOND_STEP_METHODS)
    device_name = models.CharField(max_length=127)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
