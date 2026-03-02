# accounts/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import VendorImage

@receiver(pre_save, sender=VendorImage)
def notify_vendor_image_status(sender, instance, **kwargs):
    if not instance.pk:
        return  # new upload, ignore

    old_instance = VendorImage.objects.get(pk=instance.pk)
    old_status = old_instance.status
    new_status = instance.status

    if old_status == new_status:
        return  # status didn't change

    vendor_email = instance.vendor.user.email
    vendor_name = instance.vendor.user.username
    business_name = instance.vendor.business_name

    if new_status == 'approved':
        send_mail(
            'Image Approved – I Do In Greece',
            f"Dear {vendor_name},\n\nYour uploaded image for {business_name} has been approved and is now visible in your gallery.\n\nThe I Do In Greece Team",
            'no-reply@yourdomain.com',
            [vendor_email],
            fail_silently=False
        )
    elif new_status == 'rejected':
        send_mail(
            'Image Rejected – I Do In Greece',
            f"Dear {vendor_name},\n\nYour uploaded image for {business_name} has been rejected. Please review the guidelines and upload again if appropriate.\n\nThe I Do In Greece Team",
            'no-reply@yourdomain.com',
            [vendor_email],
            fail_silently=False
        )