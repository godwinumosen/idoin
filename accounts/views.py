from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import VendorSignupForm
from django.core.mail import send_mail

# Signup view
def signup_view(request):
    if request.method == "POST":
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 'pending'  # default
            user.save()
            form.save_m2m()  # if needed
            # Send email to user confirming registration
            send_mail(
                'Registration Received',
                'Thank you for registering. Your account is pending approval.',
                'no-reply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = VendorSignupForm()
    return render(request, "accounts/signup.html", {"form": form})




# views.py or a custom authentication backend
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.status == 'approved':
                login(request, user)
                return redirect('dashboard')
            elif user.status == 'pending':
                messages.error(request, "Your account is pending approval")
            else:  # rejected
                messages.error(request, "Your account has been rejected")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')


# Dashboard view
@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")