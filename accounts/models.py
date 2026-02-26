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

    # ✅ NEW FIELDS
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    county_of_residence = models.CharField(max_length=100, null=True, blank=True)

    profile_image = models.ImageField(
        upload_to="vendor_profiles/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.business_name
    

class VendorImage(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    vendor = models.ForeignKey(
        VendorProfile,
        on_delete=models.CASCADE,
        related_name="gallery"
    )
    image = models.ImageField(upload_to="vendor_gallery/")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor.business_name} - {self.status}"