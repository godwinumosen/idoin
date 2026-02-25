from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class VendorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="vendorprofile"
    )
    business_name = models.CharField(max_length=255)
    bio = models.TextField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.business_name