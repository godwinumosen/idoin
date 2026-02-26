from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
                subject='Registration Received',
                message=(
                    f"Dear {user.username},\n\n"
                    "Thank you for registering with I Do In Greece. "
                    "We are delighted to receive your application to join our trusted vendor directory.\n\n"
                    "Your account has been successfully created and is currently pending review by our administrative team. "
                    "This approval process allows us to maintain the highest standards of quality, reliability, and professionalism "
                    "across our platform.\n\n"
                    "Once your account has been reviewed and approved, you will receive a confirmation email with further instructions. "
                    "If any additional information is required during the review process, our team will contact you directly.\n\n"
                    "We truly appreciate your interest in partnering with I Do In Greece and look forward to potentially showcasing "
                    "your services to couples planning their special day.\n\n"
                    "Warm regards,\n"
                    "The I Do In Greece Team"
                ),
                from_email='no-reply@yourdomain.com',
                recipient_list=[user.email],
                fail_silently=False,
            )
            messages.success(request, "Your account has been created and is pending approval.")
            return redirect('login')
    else:
        form = VendorSignupForm()
    return render(request, "accounts/signup.html", {"form": form})


# Login view
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
            else:
                messages.error(request, "Your account has been rejected")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'accounts/login.html')


# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



# Edit profile
@login_required
def edit_profile(request):
    # Safely get or create vendor profile
    profile, created = VendorProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "business_name": "",
            "bio": "",
            "location": "",
        }
    )

    if request.method == "POST":
        form = VendorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("dashboard")
    else:
        form = VendorProfileForm(instance=profile)

    return render(request, "accounts/edit_profile.html", {"form": form})


# Upload image (AJAX)
@login_required
def upload_gallery_image(request):
    # Safely get or create vendor profile
    profile, created = VendorProfile.objects.get_or_create(
        user=request.user,
        defaults={
            "business_name": "",
            "bio": "",
            "location": "",
        }
    )

    if request.user.status != "approved":
        return JsonResponse({"error": "Account not approved"}, status=403)

    if profile.gallery.count() >= 10:
        return JsonResponse({"error": "Gallery full"}, status=400)

    if request.method == "POST":
        image = request.FILES.get("image")
        if image:
            VendorImage.objects.create(vendor=profile, image=image)
            return JsonResponse({"success": True})

    return JsonResponse({"error": "No image uploaded"}, status=400)

# Dashboard
@login_required
def dashboard(request):
    # Default values
    profile = None
    gallery = VendorImage.objects.none()

    if request.user.is_vendor:
        try:
            profile = request.user.vendorprofile
            gallery = profile.gallery.all()

            # Check if profile is incomplete (any required fields empty)
            required_fields = ['business_name', 'bio', 'location']
            incomplete = any(not getattr(profile, field) for field in required_fields)

            if incomplete:
                # Redirect vendor to edit their profile
                messages.warning(request, "Please complete your profile before accessing the dashboard.")
                return redirect('edit_profile')

        except VendorProfile.DoesNotExist:
            # If profile somehow doesn't exist, redirect to signup (unlikely)
            messages.warning(request, "Please complete your profile first.")
            return redirect('edit_profile')

    user_info = {
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "date_joined": request.user.date_joined,
        "is_vendor": request.user.is_vendor,
        "status": request.user.status if request.user.is_vendor else None,
    }

    return render(
        request,
        "accounts/dashboard.html",
        {
            "profile": profile,
            "gallery": gallery,
            "user_info": user_info
        }
    )



# Delete image
@login_required
def delete_image(request, image_id):
    try:
        image = VendorImage.objects.get(id=image_id)
        if image.vendor.user == request.user:
            image.delete()
            messages.success(request, "Image deleted successfully!")
    except VendorImage.DoesNotExist:
        messages.error(request, "Image not found.")
    return redirect("dashboard")

