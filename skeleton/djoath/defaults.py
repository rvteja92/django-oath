from django.conf import settings

DEFAULTS = {
    'DEFAULT_ENCRYPTION_ALGORITHM': 'AES',
    'DEFAULT_ENCRYPTION_MODE': 'CBC',
    'DEFAULT_OATH_METHOD': 'TOTP',
}


class AppSettings(object):
    def __init__(self):
        for key in DEFAULTS:
            setattr(self, key, DEFAULTS[key])
            if hasattr(settings, key):
                setattr(self, key, getattr(settings, key))

app_settings = AppSettings()
