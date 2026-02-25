from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import VendorSignupForm

# Signup view
def signup_view(request):
    form = VendorSignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)  # log in immediately after signup
        return redirect("login")
    return render(request, "accounts/signup.html", {"form": form})

# Dashboard view
@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")