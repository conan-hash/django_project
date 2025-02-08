from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass



class AQIValue(models.Model):
    value = models.IntegerField(default=0)  # Stores the latest AQI value
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updates on change