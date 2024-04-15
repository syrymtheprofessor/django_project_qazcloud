from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "FALSE"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c6-a#snr7fk=0gke!q8=gt74a+x1o525ozr*w5pys(j1eb85@$"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
