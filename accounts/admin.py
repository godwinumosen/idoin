from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, VendorProfile

# Register your custom User model
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass  # inherit default behavior, you can customize if needed

# Register VendorProfile too
@admin.register(VendorProfile)
class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "business_name", "location")