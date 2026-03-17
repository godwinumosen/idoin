from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def compress_image(image, max_size=(1024, 1024), quality=70):
    try:
        img = Image.open(image)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.thumbnail(max_size)

        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=quality)
        buffer.seek(0)

        return InMemoryUploadedFile(
            buffer,
            'ImageField',
            image.name.split('.')[0] + ".jpg",
            'image/jpeg',
            sys.getsizeof(buffer),
            None
        )
    except Exception:
        return image
    
    

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
    profile_image = CloudinaryField(folder="vendor_profiles/", null=True, blank=True)

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

    def save(self, *args, **kwargs):
        if self.profile_image:
            self.profile_image = compress_image(self.profile_image)
        super().save(*args, **kwargs)

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
    image = CloudinaryField(folder="vendor_gallery/", null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.vendor.business_name} - {self.status}"
    


