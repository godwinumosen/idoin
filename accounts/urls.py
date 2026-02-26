from django.urls import path
from .views import (
    signup_view, custom_login_view, logout_view,
    dashboard, edit_profile,
    upload_gallery_image, delete_image
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", custom_login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path("upload-image/", upload_gallery_image, name="upload_image"),
    path("delete-image/<int:image_id>/", delete_image, name="delete_image"),
]