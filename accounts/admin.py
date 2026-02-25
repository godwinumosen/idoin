from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.mail import send_mail
from .models import User, VendorProfile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_vendor', 'status')
    actions = ['approve_users', 'reject_users']

    def approve_users(self, request, queryset):
        for user in queryset:
            user.status = 'approved'
            user.save()
            send_mail(
                'Account Approved',
                'Your account has been approved. You can now log in.',
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )
        self.message_user(request, "Selected users have been approved.")
    approve_users.short_description = "Approve selected users"

    def reject_users(self, request, queryset):
        for user in queryset:
            user.status = 'rejected'
            user.save()
            send_mail(
                'Account Rejected',
                'Your account has been rejected by admin.',
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )
        self.message_user(request, "Selected users have been rejected.")
    reject_users.short_description = "Reject selected users"


@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "business_name", "location")