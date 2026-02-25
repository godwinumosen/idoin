from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import VendorSignupForm
from .models import VendorProfile


def vendor_signup(request):
    if request.method == "POST":
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = VendorSignupForm()

    return render(request, "accounts/signup.html", {"form": form})


@login_required
def dashboard(request):
    vendor = VendorProfile.objects.get(user=request.user)
    return render(request, "accounts/dashboard.html", {"vendor": vendor})