from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    bio = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.business_name