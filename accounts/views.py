from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import VendorSignupForm
from django.contrib.auth.decorators import login_required

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = VendorSignupForm()
    return render(request, "accounts/signup.html", {"form": form})

# Dashboard view
@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html", {})