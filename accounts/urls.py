from django.urls import path
from .views import (
    admin_dashboard, approve_gallery, approve_vendor, dashboard_directory,
    delete_vendor, reject_gallery, reject_vendor, vendor_directory, vendor_profile_detail,
    signup_view, custom_login_view, logout_view,
    dashboard, edit_profile,
    upload_gallery_image, delete_image
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", custom_login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path('dashboard_directory/', dashboard_directory, name='dashboard_directory'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),

    # Vendor actions
    path('dashboard/vendor/<int:user_id>/approve/', approve_vendor, name='approve_vendor'),
    path('dashboard/vendor/<int:user_id>/reject/', reject_vendor, name='reject_vendor'),
    path('dashboard/vendor/<int:user_id>/delete/', delete_vendor, name='delete_vendor'),

    # Gallery actions
    path('dashboard/gallery/<int:image_id>/approve/', approve_gallery, name='approve_gallery'),
    path('dashboard/gallery/<int:image_id>/reject/', reject_gallery, name='reject_gallery'),

    # Vendor dashboard/profile
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("upload-image/", upload_gallery_image, name="upload_image"),
    path("delete-image/<int:image_id>/", delete_image, name="delete_image"),
    path("vendors/", vendor_directory, name="vendor_directory"),
    path("vendors/<int:user_id>/", vendor_profile_detail, name="vendor_profile_detail"),
]