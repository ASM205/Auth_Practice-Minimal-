from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUser already has username, password, and email.
    # We can just make the email unique here.
    email = models.Column(models.EmailField(unique=True))