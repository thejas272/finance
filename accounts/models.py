from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
  
  ROLE_CHOICES = [
    ("viewer","Viewer"),
    ("analyst","Analyst"),
    ("admin","Admin"),
  ]

  role = models.CharField(max_length=200, null=False, blank=False, choices=ROLE_CHOICES, default="viewer")
