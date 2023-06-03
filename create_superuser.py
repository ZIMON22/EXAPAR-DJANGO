import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

User = get_user_model()

username = "admin"
password = "admin"
email = "admin@mail.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser creado exitosamente.")
else:
    print("El superusuario ya existe.")
