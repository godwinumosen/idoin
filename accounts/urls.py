from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, dashboard,custom_login_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", custom_login_view, name="login"), 
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]