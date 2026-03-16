from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField



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




CATEGORY_CHOICES = (
    ('Planner', 'Planner'),
    ('Venue', 'Venue'),
    ('Florist', 'Florist'),
    ('Photographer', 'Photographer'),
    ('Videographer', 'Videographer'),
    ('DJ & Entertainment', 'DJ & Entertainment'),
    ('Hair & Makeup', 'Hair & Makeup'),
    ('Catering', 'Catering'),
    ('Wedding Cake', 'Wedding Cake'),
    ('Transport', 'Transport'),
    ('Officiant', 'Officiant'),
    ('Accommodation', 'Accommodation'),
    ('Other', 'Other'),
)



category = models.CharField(
    max_length=50,
    choices=CATEGORY_CHOICES,
    null=True,
    blank=True
)

class VendorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="vendorprofile"
    )

    business_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=1000)
    location = models.CharField(max_length=255)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True
    )

    phone_number = models.CharField(max_length=20, null=True, blank=True)
    #profile_image = models.ImageField(upload_to="vendor_profiles/", null=True, blank=True)
    profile_image = CloudinaryField("vendor_profiles/", null=True, blank=True)

    # ✅ Social links
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)

    subscription_type = models.CharField(
        max_length=10,
        choices=[('free', 'Free'), ('paid', 'Paid')],
        default='free'
    )

    subscription_expiry = models.DateField(null=True, blank=True)

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
    #image = models.ImageField(upload_to="vendor_gallery/")
    image = CloudinaryField("vendor_gallery/")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor.business_name} - {self.status}"
    


