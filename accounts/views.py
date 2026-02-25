from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import VendorProfileForm, VendorSignupForm
from .models import VendorProfile, VendorImage
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







@login_required
def edit_profile(request):
    profile = request.user.vendorprofile

    if request.method == "POST":
        form = VendorProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = VendorProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})



@login_required
def upload_gallery_image(request):
    profile = request.user.vendorprofile

    # Prevent upload if not approved
    if request.user.status != "approved":
        return redirect("dashboard")

    # Limit to 10 images
    if profile.gallery.count() >= 10:
        return redirect("dashboard")

    if request.method == "POST":
        image = request.FILES.get("image")
        if image:
            VendorImage.objects.create(
                vendor=profile,
                image=image
            )

    return redirect("dashboard")



@login_required
def dashboard(request):
    profile = request.user.vendorprofile
    gallery = profile.gallery.all()

    return render(
        request,
        "accounts/dashboard.html",
        {
            "profile": profile,
            "gallery": gallery
        }
    )


@login_required
def delete_image(request, image_id):
    image = VendorImage.objects.get(id=image_id)

    # Security check (vendor can delete only their own images)
    if image.vendor.user == request.user:
        image.delete()

    return redirect("dashboard")