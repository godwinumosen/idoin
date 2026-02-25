from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.mail import send_mail
from django.urls import path
from django.utils.html import format_html
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import User, VendorProfile, VendorImage

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_vendor', 'status', 'action_buttons')
    actions = ['approve_users', 'reject_users']

    # Dropdown actions remain
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

    # New column with Approve and Reject buttons
    def action_buttons(self, obj):
        if obj.status == 'pending':
            return format_html(
                '<a class="button" style="margin-right:5px;" href="approve/{0}/">Approve</a>'
                '<a class="button" style="background:red;color:white;" href="reject/{0}/">Reject</a>',
                obj.pk
            )
        return "Action completed"
    action_buttons.short_description = 'Actions'
    action_buttons.allow_tags = True

    # Custom URLs for button clicks
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('approve/<int:user_id>/', self.admin_site.admin_view(self.approve_single_user), name='accounts_user_approve'),
            path('reject/<int:user_id>/', self.admin_site.admin_view(self.reject_single_user), name='accounts_user_reject'),
        ]
        return custom_urls + urls


    # Approve single user view
    def approve_single_user(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        if user.status != 'approved':
            user.status = 'approved'
            user.save()

            # Send professional personalized approval email
            send_mail(
                'Account Approved – I Do In Greece',
                f"Dear {user.username},\n\n"
                "We are pleased to inform you that your vendor account with I Do In Greece has been officially approved. "
                "You can now log in to your account and start showcasing your services to couples planning their special day.\n\n"
                "To log in, please visit: https://yourdomain.com/login\n\n"
                "We are excited to have you as part of our trusted vendor network and look forward to helping you connect with potential clients.\n\n"
                "If you have any questions or need assistance, please do not hesitate to contact our support team.\n\n"
                "Warm regards,\n"
                "The I Do In Greece Team",
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )

            self.message_user(request, f"User {user.username} has been approved.", level=messages.SUCCESS)
        return redirect(request.META.get('HTTP_REFERER'))
        
    

    # Reject single user view
    def reject_single_user(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        if user.status != 'rejected':
            user.status = 'rejected'
            user.save()

            # Send professional personalized rejection email
            send_mail(
                'Account Rejected – I Do In Greece',
                f"Dear {user.username},\n\n"
                "We regret to inform you that your vendor account with I Do In Greece has been reviewed and cannot be approved at this time. "
                "This decision was made after careful consideration to ensure our platform maintains the highest standards of quality and reliability.\n\n"
                "If you believe there has been an error or would like further clarification, please contact our support team for assistance.\n\n"
                "We appreciate your interest in partnering with I Do In Greece and thank you for your understanding.\n\n"
                "Warm regards,\n"
                "The I Do In Greece Team",
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )

            self.message_user(
                request,
                f"User {user.username} has been rejected.",
                level=messages.WARNING
            )
        return redirect(request.META.get('HTTP_REFERER'))



# VendorProfile remains unchanged
@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "business_name", "location")

# VendorImage remains unchanged
@admin.register(VendorImage)
class VendorImageAdmin(admin.ModelAdmin):
    list_display = ("vendor", "status", "uploaded_at")
    list_filter = ("status",)
    list_editable = ("status",)